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
        context['city'] = self.request.GET.get('city', u'附近')
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


class NearByPointsView(TemplateView):
    template_name = "points.html"

    def get_context_data(self, **kwargs):
        context = super(NearByPointsView, self).get_context_data(**kwargs)
        context['city'] = self.request.GET.get('city', u'附近')
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


class PointsViewSet(generics.ListAPIView):
    queryset = Point.objects.filter(status=1)
    serializer_class = PointSerializer


class PointView(generics.RetrieveAPIView):
    queryset = Point.objects.filter(status=1)
    serializer_class = PointSerializer
