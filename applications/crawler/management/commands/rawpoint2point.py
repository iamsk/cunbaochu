# -*- coding: utf-8 -*-
import json
import djclick as click
from copy import deepcopy

from applications.crawler.models import RawPoint
from applications.web.models import Point


def build_for_1(data):
    d = deepcopy(data)
    d['service_time'] = data['serviceTime']
    del d['serviceTime']
    return d


def build_for_3(data):
    d = dict()
    d['province'] = ''
    d['city'] = ''
    d['district'] = ''
    d['name'] = data['name']
    d['address'] = data['address']
    d['longitude'] = data['lng']
    d['latitude'] = data['lat']
    d['linkman'] = ''
    d['telephone'] = ''
    d['service_time'] = ''
    return d


@click.command()
@click.option('--source', help='The source to do.')
def command(source):
    source = int(source)
    raw_points = RawPoint.objects.filter(status=1, source=source)
    for raw_point in raw_points:
        if not raw_point.address or len(raw_point.address) == 0:
            continue
        data = json.loads(raw_point.raw_data)
        try:
            Point.objects.get(address=raw_point.address)
            print 'same address: {}'.format(raw_point.address)
            continue
        except Point.DoesNotExist:
            print source
            if source == 1:
                d = build_for_1(data)
            elif source == 3:
                d = build_for_3(data)
            p = Point(**d)
            p.save()


if __name__ == '__main__':
    command()
