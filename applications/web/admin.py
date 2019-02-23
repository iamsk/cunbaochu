# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Point


class PointAdmin(admin.ModelAdmin):
    list_display = ('raw_point', 'store_type', 'identity', 'name', 'address', 'status')


admin.site.register(Point, PointAdmin)
