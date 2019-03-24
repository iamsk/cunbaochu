# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import RawPoint, SubmittedPoint


class RawPointAdmin(admin.ModelAdmin):
    list_display = ('source', 'identity', 'address', 'status')
    search_fields = ('address',)
    list_filter = ('source',)


class SubmittedPointAdmin(admin.ModelAdmin):
    list_display = ('source', 'name', 'store_type', 'address', 'longitude', 'latitude', 'status')
    search_fields = ('address',)


admin.site.register(RawPoint, RawPointAdmin)

admin.site.register(SubmittedPoint, SubmittedPointAdmin)
