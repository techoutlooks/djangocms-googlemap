# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals


def get_setting(name):
    from django.conf import settings
    from django.utils.translation import ugettext_lazy as _
    from meta import settings as meta_settings
   
    DJANGOCMS_GOOGLEMAP_DEFAULT_TEMPLATES = (("djangocms_googlemap/googlemap.html", _("Default")),)

    default = {
      
        # todo: fix: string to tuple mismatch
        'DJANGOCMS_GOOGLEMAP_TEMPLATES': getattr(settings, "DJANGOCMS_GOOGLEMAP_TEMPLATES", DJANGOCMS_GOOGLEMAP_DEFAULT_TEMPLATES),

    }
    
    # return setting from 'djangocms_blog.get_setting' if not found in 'default'  
    setting = default.get('DJANGOCMS_GOOGLEMAP_%s' % name)
    if not setting:
        try: 
            from djangocms_blog.settings import get_setting as _get_setting
            setting = _get_setting(name)
        except KeyError:
            setting = None
    return setting

