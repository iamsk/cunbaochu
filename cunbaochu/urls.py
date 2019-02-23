"""cunbaochu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from applications.web import views

schema_view = get_swagger_view(title='cunbaochu API')

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^nearby/$', views.NearByView.as_view()),
    url(r'^search/$', views.PointsViewSet.as_view()),
    url(r'^points/(?P<pk>[0-9]+)/$', views.PointView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/$', schema_view)
]
