# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from rest_framework import generics

from applications.web.models import Point
from applications.web.serializers import PointSerializer
from applications.web.documents import PointDocument


class IndexView(TemplateView):
    template_name = "index.html"


class NearByView(TemplateView):
    template_name = "nearby.html"

    def get_context_data(self, **kwargs):
        context = super(NearByView, self).get_context_data(**kwargs)
        context['city'] = self.kwargs.get('city', u'附近')
        longitude = self.kwargs.get('longitude', '116.232922')
        latitude = self.kwargs.get('latitude', '39.542637')
        s = PointDocument.search().filter('geo_distance', distance='1000000m',
                                          location={"lat": latitude, "lon": longitude})[:10]
        points = s.execute()
        context['points'] = points
        return context


class PointsViewSet(generics.ListAPIView):
    queryset = Point.objects.filter(status=1)
    serializer_class = PointSerializer


class PointView(generics.RetrieveAPIView):
    queryset = Point.objects.filter(status=1)
    serializer_class = PointSerializer
