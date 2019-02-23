# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import shortuuid
from django.db import models

from applications.crawler.models import RawPoint


class Point(models.Model):
    STORE_TYPES = (
        (1, 'small'),
        (2, 'medium'),
        (3, 'large'),
    )
    STATUSES = (
        (0, u'禁用'),
        (1, u'正常'),
    )
    raw_point = models.ForeignKey(RawPoint)
    store_type = models.SmallIntegerField(choices=STORE_TYPES, default=1)
    identity = models.CharField(max_length=100, help_text=u'唯一标识', default=shortuuid.uuid)
    province = models.CharField(max_length=50, help_text=u'省')
    city = models.CharField(max_length=50, help_text=u'市')
    district = models.CharField(max_length=50, help_text=u'区')
    name = models.CharField(max_length=100, help_text=u'名称')
    address = models.CharField(max_length=200, help_text=u'地址')
    longitude = models.CharField(max_length=100, help_text=u'经度')
    latitude = models.CharField(max_length=100, help_text=u'纬度')
    linkman = models.CharField(max_length=20, help_text=u'联系人')
    telephone = models.CharField(max_length=20, help_text=u'联系电话')
    service_time = models.CharField(max_length=100, help_text=u'服务时间')
    status = models.SmallIntegerField(choices=STATUSES, default=1)

    def __unicode__(self):
        return '{}:{}:{}:{}'.format(self.store_type, self.identity, self.name, self.address)

    class Meta:
        unique_together = (('identity',), ('raw_point',))
