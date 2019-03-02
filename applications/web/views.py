# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from rest_framework import generics

from applications.web.models import Point
from applications.web.serializers import PointSerializer
from applications.web.documents import PointDocument


class IndexView(TemplateView):
    template_name = "index.html"


class POIView(TemplateView):
    template_name = "nearby.html"

    def get_context_data(self, **kwargs):
        context = super(POIView, self).get_context_data(**kwargs)
        context['city'] = self.request.GET.get('city', u'北京')
        longitude = self.request.GET.get('longitude', '116.344251')
        latitude = self.request.GET.get('latitude', '40.034957')
        location = {"lat": latitude, "lon": longitude}
        s = PointDocument.search().sort(
            {"_geo_distance": {
                'location': location,
                "order": "asc",
                "unit": "km"
            }}
        )
        points = s.execute()
        context['points'] = points[:20]
        return context


class NearByView(TemplateView):
    template_name = "nearby.html"

    def get_context_data(self, **kwargs):
        context = super(NearByView, self).get_context_data(**kwargs)
        context['city'] = self.request.GET.get('city', u'附近')
        return context


class NearByPointsView(TemplateView):
    template_name = "points.html"

    def get_context_data(self, **kwargs):
        context = super(NearByPointsView, self).get_context_data(**kwargs)
        longitude = self.request.GET.get('longitude', '116.344251')
        latitude = self.request.GET.get('latitude', '40.034957')
        location = {"lat": latitude, "lon": longitude}
        s = PointDocument.search().sort(
            {"_geo_distance": {
                'location': location,
                "order": "asc",
                "unit": "km"
            }}
        )
        points = s.execute()
        context['points'] = points[:20]
        return context


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
        return points


class SearchView(PointMixin, generics.ListAPIView):
    queryset = Point.objects.filter(status=1)
    serializer_class = PointSerializer

    def get_queryset(self):
        lon = self.request.GET.get('longitude', '116.344251')
        lat = self.request.GET.get('latitude', '40.034957')
        return self.get_points_by_lon_lat(lon, lat)


class PointView(generics.RetrieveAPIView):
    queryset = Point.objects.filter(status=1)
    serializer_class = PointSerializer
