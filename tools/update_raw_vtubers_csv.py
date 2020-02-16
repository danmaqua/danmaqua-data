#!/usr/bin/env python3
# encoding: UTF8
from os import listdir, mkdir
from os.path import isfile, join, abspath
import csv
import requests

GET_ROOM_INIT_API = 'https://api.live.bilibili.com/room/v1/Room/room_init?id=%s'
GET_SPACE_INFO_API = 'https://api.bilibili.com/x/space/acc/info?mid=%s'

VTUBER_FIELD_NAMES = ['uid', 'room', 'name', 'group', 'description', 'face']

def main():
    csv_path = '../raw/vtubers'
    csv_files = [f for f in listdir(csv_path) if isfile(join(csv_path, f))]
    for csv_file in csv_files:
        items = []
        with open(join(csv_path, csv_file), mode='r', encoding='utf-8') as f_obj:
            reader = csv.DictReader(f_obj)
            items.extend(list(reader))
        for item in items:
            if not item['uid'] or len(item['uid'].strip()) <= 0:
                r = requests.get(GET_ROOM_INIT_API % item['room'])
                r.raise_for_status()
                rep_json = r.json()
                item['uid'] = rep_json['data']['uid']
            r = requests.get(GET_SPACE_INFO_API % item['uid'])
            r.raise_for_status()
            rep_json = r.json()
            item['name'] = rep_json['data']['name']
            item['face'] = rep_json['data']['face']
            print(item)
        with open(join(csv_path, csv_file), mode='w', encoding='utf-8') as f_obj:
            writer = csv.DictWriter(f_obj, fieldnames=VTUBER_FIELD_NAMES)
            writer.writeheader()
            writer.writerows(items)

if __name__ == '__main__':
    main()