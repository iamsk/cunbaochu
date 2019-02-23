# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class RawPoint(models.Model):
    SOURCES = (
        (1, 'i.sf-express.com'),
    )
    STATUSES = (
        (0, u'禁用'),
        (1, u'正常'),
    )
    source = models.SmallIntegerField(choices=SOURCES, default=1)
    identity = models.CharField(max_length=100, help_text=u'唯一标识')
    address = models.CharField(max_length=200, help_text=u'地址')
    raw_data = models.TextField(help_text=u'原始信息')
    status = models.SmallIntegerField(choices=STATUSES, default=1)

    def __unicode__(self):
        return '{}:{}:{}'.format(self.source, self.identity, self.address)

    class Meta:
        unique_together = (('source', 'identity'),)
