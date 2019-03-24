# -*- coding: utf-8 -*-
import djclick as click
import json

from applications.crawler.models import RawPoint
from applications.web.models import Point


@click.command()
@click.option('--source', help='The source to do.')
def command(source):
    raw_points = RawPoint.objects.filter(status=1, source=source)
    print raw_points
    for raw_point in raw_points:
        if not raw_point.address or len(raw_point.address) == 0:
            continue
        data = json.loads(raw_point.raw_data)
        p, created = Point.objects.get_or_create(address=raw_point.address)
        if not created:
            print 'same address: {}'.format(raw_point.address)
            continue
        if source == 1:
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
        elif source == 3:
            p.province = ''
            p.city = ''
            p.district = ''
            p.name = data['name']
            p.address = data['address']
            p.longitude = data['lng']
            p.latitude = data['lat']
            p.linkman = ''
            p.telephone = ''
            p.service_time = ''
        p.save()


if __name__ == '__main__':
    command()
