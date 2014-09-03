# coding: utf-8
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_flickr_player.models import FlickrLink


class FlickrPlayerPlugin(CMSPluginBase):
    model = FlickrLink
    name = _(u"Flickr player")
    render_template = "cms/plugins/flickr_player.html"

    def render(self, context, instance, placeholder):
        width = instance.width or getattr(settings, "CMS_FLICKR_PLAYER_WIDTH", "100%")
        height = instance.height or getattr(settings, "CMS_FLICKR_PLAYER_HEIGHT", "500")

        url = instance.url

        context.update({
            'width': width,
            'height': height,
            'url': url,
            'placeholder': placeholder,
            'object': instance
        })
        return context

plugin_pool.register_plugin(FlickrPlayerPlugin)
