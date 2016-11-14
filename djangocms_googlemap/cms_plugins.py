from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import GoogleMapForm
from .models import GoogleMap
from .settings import get_setting


class GoogleMapPlugin(CMSPluginBase):
    model = GoogleMap
    name = _("Google Map")
    render_template = get_setting('TEMPLATES')[0][0]

    admin_preview = False
    form = GoogleMapForm
    fieldsets = (
        (None, {
            'fields': ('title', 'address', ('zipcode', 'city',),
                       'content', 'zoom', ('lat', 'lng'),),
        }),
        (_('Advanced'), {
            'fields': (('route_planer', 'route_planer_title'),
                       ('width', 'height',), 'info_window', 'scrollwheel',
                       'double_click_zoom', 'draggable', 'keyboard_shortcuts',
                       'pan_control', 'zoom_control', 'street_view_control',
                       'style', 'template'),
        }),
    )

    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template

        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(GoogleMapPlugin)
