# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from applications.web.models import Point, POI
from applications.web.serializers import PointSerializer, PointCreateSerializer
from applications.web.documents import PointDocument
from applications.crawler.models import RawPoint


class PointMixin(object):
    @classmethod
    def get_points_by_lon_lat(cls, lon, lat):
        location = {"lat": lat, "lon": lon}
        s = PointDocument.search().sort(
            {"_geo_distance": {
                'location': location,
                "order": "asc",
                "unit": "km"
            }}
        )
        points = s.to_queryset()
        _points = []
        for index, p in enumerate(points):
            p.index = index
            _points.append(p)
        return _points


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pois'] = POI.objects.all()
        return context


class POIView(PointMixin, TemplateView):
    template_name = "poi.html"

    def get_context_data(self, **kwargs):
        context = super(POIView, self).get_context_data(**kwargs)
        pk = self.request.GET.get('pk', 1)
        poi = get_object_or_404(POI, id=pk)
        context['poi'] = poi
        context['points'] = self.get_points_by_lon_lat(poi.longitude, poi.latitude)
        return context


class NearByView(TemplateView):
    template_name = "nearby.html"


class NearByPointsView(PointMixin, TemplateView):
    template_name = "points.html"

    def get_context_data(self, **kwargs):
        context = super(NearByPointsView, self).get_context_data(**kwargs)
        lon = self.request.GET.get('longitude', '116.344251')
        lat = self.request.GET.get('latitude', '40.034957')
        context['points'] = self.get_points_by_lon_lat(lon, lat)
        return context


class SearchView(PointMixin, generics.ListAPIView):
    queryset = Point.objects.filter(status=1)
    serializer_class = PointSerializer

    def get_queryset(self):
        lon = self.request.GET.get('longitude', '116.344251')
        lat = self.request.GET.get('latitude', '40.034957')
        return self.get_points_by_lon_lat(lon, lat)


class PointsView(generics.CreateAPIView):
    serializer_class = PointCreateSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        p, created = RawPoint.objects.get_or_create(source=2,
                                                    identity='{},{}'.format(data['longitude'], data['latitude']))
        if created:
            p.address = data['address']
            p.raw_data = json.dumps(data)
            p.save()
        return Response(data, status=status.HTTP_201_CREATED)
