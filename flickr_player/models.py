# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


class FlickrLink(CMSPlugin):
    url = models.URLField(_("link"))
    width = models.CharField(_(u"width"), max_length=5, null=True, blank=True)
    height = models.CharField(_(u"height"), max_length=5, null=True, blank=True)

    def __unicode__(self):
        return self.url

    search_fields = ('url', )
