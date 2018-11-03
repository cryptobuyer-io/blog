from datetime import datetime

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, TabbedInterface, ObjectList
)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from utils.translation import TranslatedField


class BlogPage(Page):
    date = models.DateTimeField(
        default=datetime.today,
        verbose_name=_('Date')
    )
    date_updated = models.DateTimeField(
        default=datetime.now,
        verbose_name=_('Date Updated')
    )
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Main Image')
    )
    title_en = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Title (English)')
    )
    title_pt = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Title (Portuguese)')
    )
    intro_es = models.TextField(
        max_length=400,
        verbose_name=_('Intro (Spanish)')
    )
    intro_en = models.TextField(
        max_length=400,
        blank=True,
        verbose_name=_('Intro (English)')
    )
    intro_pt = models.TextField(
        max_length=400,
        blank=True,
        verbose_name=_('Intro (Portuguese)')
    )
    content_es = RichTextField(
        blank=True,
        verbose_name=_('Content (Spanish)')
    )
    content_en = RichTextField(
        blank=True,
        verbose_name=_('Content (English)')
    )
    content_pt = RichTextField(
        blank=True,
        verbose_name=_('Content (Portuguese)')
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Author')
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('intro_es', classname='full'),
        FieldPanel('content_es', classname='full'),
        FieldPanel('author')
    ]

    english_content_panels = [
        FieldPanel('title_en', classname='full title'),
        FieldPanel('intro_en', classname='full'),
        FieldPanel('content_en', classname='full')
    ]

    portuguese_content_panels = [
        FieldPanel('title_pt', classname='full title'),
        FieldPanel('intro_pt', classname='full'),
        FieldPanel('content_pt', classname='full')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=_('Content (Es)')),
        ObjectList(english_content_panels, heading=_('Content (En)')),
        ObjectList(portuguese_content_panels, heading=_('Content (Pt)')),
        ObjectList(Page.promote_panels, heading=_('Promote')),
        ObjectList(Page.settings_panels, heading=_('Settings'), classname="settings"),
    ])

    parent_page_types = ['home.HomePage']
    subpage_types = []

    def translated_title(self):
        from utils.translation import LANGUAGE as language
        translated_field = TranslatedField(
            'title',
            'title_en',
            'title_pt'
        )
        return translated_field.get(self, language)

    def translated_intro(self):
        from utils.translation import LANGUAGE as language
        translated_field = TranslatedField(
            'intro_es',
            'intro_en',
            'intro_pt'
        )
        return translated_field.get(self, language)

    def translated_content(self):
        from utils.translation import LANGUAGE as language
        translated_field = TranslatedField(
            'content_es',
            'content_en',
            'content_pt'
        )
        return translated_field.get(self, language)

    def serve(self, request):
        return super(BlogPage, self).serve(request)

    def get_context(self, request):
        from utils.translation import LANGUAGE as language
        context = super(BlogPage, self).get_context(request)
        context['language'] = language
        return context
