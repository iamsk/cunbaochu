# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Point, POI


class PointAdmin(admin.ModelAdmin):
    list_display = ('identity', 'name', 'store_type', 'address', 'status')


class PoiAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'order', 'longitude', 'latitude', 'status')


admin.site.register(Point, PointAdmin)
admin.site.register(POI, PoiAdmin)
