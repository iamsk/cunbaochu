# coding: utf-8
from __future__ import unicode_literals

from rest_framework import serializers

from applications.crawler.models import RawPoint


class RawPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawPoint
        fields = [
            'address',
        ]
