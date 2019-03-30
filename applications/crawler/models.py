# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class RawPoint(models.Model):
    SOURCES = (
        (1, 'i.sf-express.com'),
        (2, 'submit'),
        (3, 'cunzj.com'),
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
        return '{}:{}'.format(self.source, self.identity)

    class Meta:
        unique_together = (('source', 'identity'),)


class SubmittedPoint(models.Model):
    STORE_TYPES = (
        (1, 'small'),
        (2, 'medium'),
        (3, 'large'),
    )
    STATUSES = (
        (0, u'禁用'),
        (1, u'正常'),
    )
    source = models.CharField(max_length=200, help_text=u'来源', default='user')
    store_type = models.SmallIntegerField(choices=STORE_TYPES, default=1)
    name = models.CharField(max_length=100, help_text=u'店名')
    address = models.CharField(max_length=200, help_text=u'地址')
    longitude = models.CharField(max_length=100, help_text=u'经度')
    latitude = models.CharField(max_length=100, help_text=u'纬度')
    linkman = models.CharField(max_length=20, help_text=u'联系人', default='', blank=True)
    telephone = models.CharField(max_length=20, help_text=u'联系电话', default='', blank=True)
    service_time = models.CharField(max_length=100, help_text=u'服务时间', default='', blank=True)
    images = models.CharField(max_length=1024, help_text=u'图片', default='', blank=True)
    status = models.SmallIntegerField(choices=STATUSES, default=1)

    def __unicode__(self):
        return '{}:{}:{}'.format(self.source, self.longitude, self.latitude)

    class Meta:
        unique_together = (('source', 'longitude', 'latitude'),)
