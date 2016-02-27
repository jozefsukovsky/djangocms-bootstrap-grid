# -*- coding: utf-8 -*-

from functools import partial

from cms.models import CMSPlugin
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _, string_concat

BOOTSTRAP_GRID_CHOICES = [
    (i, string_concat(unicode(i), ' ', _('columns')))
    for i in range(1, 13)
]

ColumnSizeField = partial(
    models.IntegerField,
    default=0,
    choices=BOOTSTRAP_GRID_CHOICES,
    null=True,
    blank=True
)


class GridBootstrap(CMSPlugin):
    custom_classes = models.CharField(
        _('custom classes'),
        max_length=200,
        blank=True
    )

    def __unicode__(self):
        return _(u'%s columns') % self.cmsplugin_set.all().count()


class GridColumnBootstrap(CMSPlugin):
    size_xs = ColumnSizeField(verbose_name=_('size (xs)'))
    size_sm = ColumnSizeField(verbose_name=_('size (sm)'))
    size_md = ColumnSizeField(verbose_name=_('size (md)'))
    size_lg = ColumnSizeField(verbose_name=_('size (lg)'))

    custom_classes = models.CharField(
        verbose_name=_('custom classes'),
        max_length=200,
        blank=True
    )

    def __unicode__(self):
        result = []
        if self.size_xs:
            result.append('col-xs-%d' % self.size_xs)
        if self.size_sm:
            result.append('col-sm-%d' % self.size_sm)
        if self.size_md:
            result.append('col-md-%d' % self.size_md)
        if self.size_lg:
            result.append('col-lg-%d' % self.size_lg)
        return u' '.join(result)
