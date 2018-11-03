from __future__ import absolute_import, unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from blog.models import BlogPage
from utils.translation import TranslatedField


class HomePage(Page):
    intro_es = models.CharField(
        max_length=255,
        verbose_name=_('Introduction (Spanish)')
    )
    intro_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Introduction (English)')
    )
    intro_pt = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Introduction (Portuguese)')
    )

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Main Image')
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro_es', classname='full title'),
        FieldPanel('intro_en', classname='full title'),
        FieldPanel('intro_pt', classname='full title'),
        ImageChooserPanel('hero_image')
    ]

    subpage_types = ['blog.BlogPage']

    @property
    def blogs(self):
        # Get list of blog pages that are descendants of this page
        blogs = BlogPage.objects.descendant_of(self).live()
        blogs = blogs.order_by(
            '-date'
        )
        return blogs

    def get_context(self, request):
        from utils.translation import LANGUAGE as language
        context = super(HomePage, self).get_context(request)
        context['language'] = language

        blogs = self.blogs

        # Pagination
        page = request.GET.get('page')
        page_size = 5

        if hasattr(settings, 'BLOG_PAGINATION_PER_PAGE'):
            page_size = settings.BLOG_PAGINATION_PER_PAGE

        if page_size is not None:
            paginator = Paginator(blogs, page_size)  # Show 10 blogs per page
            try:
                blogs = paginator.page(page)
            except PageNotAnInteger:
                blogs = paginator.page(1)
            except EmptyPage:
                blogs = paginator.page(paginator.num_pages)

            if paginator.num_pages > 1:
                is_paginated = True
            else:
                is_paginated = False
        else:
            is_paginated = False

        context['blogs'] = blogs
        context['is_paginated'] = is_paginated
        return context

    def translated_intro(self):
        from utils.translation import LANGUAGE as language
        translated_field = TranslatedField(
            'intro_es',
            'intro_en',
            'intro_pt'
        )
        return translated_field.get(self, language)
