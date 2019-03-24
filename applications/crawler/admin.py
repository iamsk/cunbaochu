# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.contrib import admin
from django_admin_json_editor import JSONEditorWidget

from .models import RawPoint


class RawPointAdmin(admin.ModelAdmin):
    list_display = ('source', 'identity', 'address', 'status')
    search_fields = ('address',)
    list_filter = ('source',)

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            schema = json.loads(obj.raw_data)
        else:
            schema = {
                "type": "object", "properties": {
                    "linkman": {"type": "string"}, "name": {"type": "string"},
                    "service_time": {"type": "string"}, "userId": {"type": "string"},
                    "telephone": {"type": "string"}, "longitude": {"type": "string"},
                    "latitude": {"type": "string"}, "address": {"type": "string"}},
                "required": ["linkman", "name", "service_time", "userId", "telephone", "longitude", "latitude",
                             "address"]}
        widget = JSONEditorWidget(schema, False, True)
        form = super(RawPointAdmin, self).get_form(request, obj, widgets={'raw_data': widget}, **kwargs)
        return form


admin.site.register(RawPoint, RawPointAdmin)
