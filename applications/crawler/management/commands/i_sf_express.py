# -*- coding: utf-8 -*-
import djclick as click
import requests
import time
import json

from applications.crawler.models import RawPoint

area_list_url = 'https://i.sf-express.com/service/address/data/keyword/cn/sc'

a = {"keywordData": [{"keyword": "东城区", "countyname": "东城区", "countyid": "499", "cityname": "北京市", "cityid": "010",
                      "provincename": "北京市", "provinceid": "010", "showtext": "北京市 北京市 东城区", "country_code": "CN",
                      "lang_code": "sc", "id": None, "createTm": None, "modifiedTm": None}, ]}

point_list_url = 'https://i.sf-express.com/service/new/commonquery/queryNearlyStore?_=1550587844255'

# address: 北京市北京市西城区西城区
# type: 1
# lat: null
# lng: null
# storeType: 3,1,2,4,5
# keyword:

b = {"data": [{"address": "北京市北京市西城区西城区", "name": None, "serviceTime": None, "code": None, "city": None, "cityId": None,
               "storeType": None, "distance": None, "provinceId": None, "province": None, "deptCode": None,
               "longitude": None, "latitude": None, "telephone": None, "serviceContent": None, "district": None,
               "linkman": None, "addressEn": None, "longitudeBaidu": "116.37319", "latitudeBaidu": "39.93428",
               "districtId": None, "serviceTime6": None, "serviceTime7": None, "serviceTime0": None},
              ], "code": "ok", "success": True}


@click.command()
def command():
    data = requests.get(area_list_url).json()
    area_list = data['keywordData']
    for area in area_list:
        address = u'{}{}{}'.format(area['provincename'], area['cityname'], area['countyname'])
        params = {'address': address, 'type': 1, 'lat': None, 'lng': None, 'storeType': '3,1,2,4,5', 'keyword': ''}
        data = requests.post(point_list_url, params).json()
        point_list = data['data']
        print address, len(point_list) if point_list else 0
        if not point_list:
            continue
        for point in point_list:
            if not point['code']:
                continue
            p, created = RawPoint.objects.get_or_create(source=1, identity=point['code'])
            if created:
                print point['address']
                p.address = point['address']
                p.raw_data = json.dumps(point)
                p.save()
        time.sleep(10)


if __name__ == '__main__':
    command()
