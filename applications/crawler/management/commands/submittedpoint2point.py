# -*- coding: utf-8 -*-
import djclick as click

from applications.crawler.models import SubmittedPoint
from applications.web.models import Point


@click.command()
def command():
    raw_points = SubmittedPoint.objects.filter(status=1)
    for raw_point in raw_points:
        p, created = Point.objects.get_or_create(longitude=raw_point.longitude, latitude=raw_point.latitude)
        if not created:
            continue
        p.province = ''
        p.city = ''
        p.district = ''
        p.name = raw_point.name
        p.address = raw_point.address
        p.longitude = raw_point.longitude
        p.latitude = raw_point.latitude
        p.linkman = raw_point.linkman
        p.telephone = raw_point.telephone
        p.service_time = raw_point.service_time
        p.save()


if __name__ == '__main__':
    command()
