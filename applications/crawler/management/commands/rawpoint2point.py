# -*- coding: utf-8 -*-
import djclick as click
import json

from applications.crawler.models import RawPoint
from applications.web.models import Point


@click.command()
def command():
    raw_points = RawPoint.objects.filter(status=1)
    for raw_point in raw_points:
        if not raw_point.address or len(raw_point.address) == 0:
            continue
        data = json.loads(raw_point.raw_data)
        p, _ = Point.objects.get_or_create(raw_point=raw_point)
        p.province = data['province']
        p.city = data['city']
        p.district = data['district']
        p.name = data['name']
        p.address = data['address']
        p.longitude = data['longitude']
        p.latitude = data['latitude']
        p.linkman = data['linkman']
        p.telephone = data['telephone']
        p.service_time = data['serviceTime']
        p.save()


if __name__ == '__main__':
    command()
