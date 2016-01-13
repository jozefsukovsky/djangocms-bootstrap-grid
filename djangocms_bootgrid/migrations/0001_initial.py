# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='GridBootstrap',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('custom_classes', models.CharField(max_length=200, verbose_name='custom classes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GridColumnBootstrap',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('size_xs', models.IntegerField(default=0, null=True, verbose_name='size (xs)', blank=True, choices=[(1, '1 columns'), (2, '2 columns'), (3, '3 columns'), (4, '4 columns'), (5, '5 columns'), (6, '6 columns'), (7, '7 columns'), (8, '8 columns'), (9, '9 columns'), (10, '10 columns'), (11, '11 columns'), (12, '12 columns')])),
                ('size_sm', models.IntegerField(default=0, null=True, verbose_name='size (sm)', blank=True, choices=[(1, '1 columns'), (2, '2 columns'), (3, '3 columns'), (4, '4 columns'), (5, '5 columns'), (6, '6 columns'), (7, '7 columns'), (8, '8 columns'), (9, '9 columns'), (10, '10 columns'), (11, '11 columns'), (12, '12 columns')])),
                ('size_md', models.IntegerField(default=0, null=True, verbose_name='size (md)', blank=True, choices=[(1, '1 columns'), (2, '2 columns'), (3, '3 columns'), (4, '4 columns'), (5, '5 columns'), (6, '6 columns'), (7, '7 columns'), (8, '8 columns'), (9, '9 columns'), (10, '10 columns'), (11, '11 columns'), (12, '12 columns')])),
                ('size_lg', models.IntegerField(default=0, null=True, verbose_name='size (lg)', blank=True, choices=[(1, '1 columns'), (2, '2 columns'), (3, '3 columns'), (4, '4 columns'), (5, '5 columns'), (6, '6 columns'), (7, '7 columns'), (8, '8 columns'), (9, '9 columns'), (10, '10 columns'), (11, '11 columns'), (12, '12 columns')])),
                ('custom_classes', models.CharField(max_length=200, verbose_name='custom classes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
