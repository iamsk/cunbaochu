# coding: utf-8
from __future__ import unicode_literals

from rest_framework import serializers

from applications.web.models import Point
from applications.crawler.models import SubmittedPoint


class PointSerializer(serializers.ModelSerializer):
    index = serializers.IntegerField()
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()

    class Meta:
        model = Point
        fields = [
            'index',
            'identity',
            'name',
            'address',
            'longitude',
            'latitude',
            'service_time',
        ]


class PointCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedPoint
        fields = '__all__'
