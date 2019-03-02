# coding: utf-8
from __future__ import unicode_literals

from rest_framework import serializers

from applications.web.models import Point


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = [
            'identity',
            'name',
            'address',
            'longitude',
            'latitude',
            'service_time',
        ]
