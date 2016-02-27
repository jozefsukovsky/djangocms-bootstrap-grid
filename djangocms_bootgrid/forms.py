# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import (
    GridBootstrap,
    BOOTSTRAP_GRID_CHOICES,
    GridColumnBootstrap
)

COLUMN_SIZE_CHOICES = [('', '----------')] + BOOTSTRAP_GRID_CHOICES
NUM_COLUMNS = [
    (i, '%s' % i) for i in range(0, 12)
]


class GridPluginForm(forms.ModelForm):
    create = forms.ChoiceField(
        choices=NUM_COLUMNS,
        label=_('Create Columns'),
        help_text=_('Create this number of columns inside')
    )
    create_size_xs = forms.ChoiceField(
        choices=COLUMN_SIZE_CHOICES,
        label=_('Column size (xs)'),
        help_text=(
            'Width of created columns. You can still change the \
width of the column afterwards.'),
        required=False
    )
    create_size_sm = forms.ChoiceField(
        choices=COLUMN_SIZE_CHOICES,
        label=_('Column size (sm)'),
        help_text=(
            'Width of created columns. You can still change the width of \
the column afterwards.'),
        required=False
    )
    create_size_md = forms.ChoiceField(
        choices=COLUMN_SIZE_CHOICES,
        label=_('Column size (md)'),
        help_text=(
            'Width of created columns. You can still change the width of the \
column afterwards.'),
        required=False
    )
    create_size_lg = forms.ChoiceField(
        choices=COLUMN_SIZE_CHOICES,
        label=_('Column size (lg)'),
        help_text=(
            'Width of created columns. You can still change the width of the \
column afterwards.'),
        required=False
    )

    class Meta:
        model = GridBootstrap
        exclude = (
            'page', 'position', 'placeholder', 'language', 'plugin_type')


class GridColumnPluginForm(forms.ModelForm):

    class Meta:
        model = GridColumnBootstrap
        fields = '__all__'

    def clean(self):
        data = super(GridColumnPluginForm, self).clean()
        sizes = [
            data['size_xs'],
            data['size_sm'],
            data['size_md'],
            data['size_lg'],
        ]
        if not any(sizes):
            raise ValidationError(_('Please provide at least one size'))
        return data
