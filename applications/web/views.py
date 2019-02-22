# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from rest_framework import generics

from applications.crawler.models import RawPoint
from applications.web.serializers import RawPointSerializer


class IndexView(TemplateView):
    template_name = "index.html"


class PointsViewSet(generics.ListAPIView):
    queryset = RawPoint.objects.filter(status=1)
    serializer_class = RawPointSerializer


class PointView(generics.RetrieveAPIView):
    queryset = RawPoint.objects.filter(status=1)
    serializer_class = RawPointSerializer
