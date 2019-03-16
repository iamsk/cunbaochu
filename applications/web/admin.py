# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Point, POI


class PointAdmin(admin.ModelAdmin):
    list_display = ('raw_point', 'store_type', 'identity', 'name', 'address', 'status')


class PoiAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'order', 'longitude', 'latitude', 'status')


admin.site.register(Point, PointAdmin)
admin.site.register(POI, PoiAdmin)
