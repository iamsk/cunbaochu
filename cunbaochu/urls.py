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
from django.conf import settings

from applications.web import views

schema_view = get_swagger_view(title='cunbaochu API')

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^pois/(?P<pk>\d+)/$', views.POIView.as_view()),
    url(r'^nearby/$', views.NearByView.as_view()),
    url(r'^nearby-points/$', views.NearByPointsView.as_view()),
    # API
    url(r'^search/$', views.SearchView.as_view()),
    url(r'^points/$', views.PointsView.as_view()),
    # management
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^docs/$', schema_view)
    ]
