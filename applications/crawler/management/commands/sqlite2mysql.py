# -*- coding: utf-8 -*-
import djclick as click

from applications.crawler.models import RawPoint


@click.command()
def command():
    raw_points = RawPoint.objects.using('sqlite').all()
    for raw_point in raw_points:
        raw_point.save()


if __name__ == '__main__':
    command()
