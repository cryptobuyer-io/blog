# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-08 13:51
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Post date')),
                ('date_updated', models.DateTimeField(default=datetime.datetime.now)),
                ('intro', models.CharField(max_length=250)),
                ('content', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('main_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]