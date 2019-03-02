# coding: utf-8
from __future__ import unicode_literals

from rest_framework import serializers

from applications.web.models import Point


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


class PointCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    longitude = serializers.CharField()
    latitude = serializers.CharField()
    service_time = serializers.CharField()
    linkman = serializers.CharField()
    telephone = serializers.CharField()
