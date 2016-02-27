# -*- coding: utf-8 -*-
from decimal import Context

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from djangocms_bootgrid.forms import GridPluginForm, GridColumnPluginForm
from djangocms_bootgrid.models import GridBootstrap, GridColumnBootstrap

class GridBootstrapPlugin(CMSPluginBase):
    model = GridBootstrap
    name = _('Grid Row (wrapper)')
    module = _('Multi Columns')
    render_template = 'djangocms_bootgrid/grid.html'
    allow_children = True
    child_classes = ['GridColumnBootstrapPlugin']
    form = GridPluginForm

    def render(self, context, instance, placeholder):
        context.update({
            'grid': instance,
            'placeholder': placeholder,
        })
        return context

    def save_model(self, request, obj, form, change):
        response = super(
            GridBootstrapPlugin,
            self).save_model(request, obj, form, change)
        if not change:
            for x in xrange(int(form.cleaned_data['create'])):
                col = GridColumnBootstrap(
                    parent=obj,
                    placeholder=obj.placeholder,
                    language=obj.language,
                    size_xs=form.cleaned_data.get('create_size_xs') or None,
                    size_sm=form.cleaned_data.get('create_size_sm') or None,
                    size_md=form.cleaned_data.get('create_size_md') or None,
                    size_lg=form.cleaned_data.get('create_size_lg') or None,
                    position=CMSPlugin.objects.filter(parent=obj).count(),
                    plugin_type=GridColumnBootstrapPlugin.__name__,
                )
                col.save()
            return response


class GridColumnBootstrapPlugin(CMSPluginBase):
    model = GridColumnBootstrap
    name = _('Grid Column')
    module = _('Multi Columns')
    render_template = 'djangocms_bootgrid/column.html'
    allow_children = True
    form = GridColumnPluginForm

    def render(self, context, instance, placeholder):
        context.update({
            'column': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(GridBootstrapPlugin)
plugin_pool.register_plugin(GridColumnBootstrapPlugin)
