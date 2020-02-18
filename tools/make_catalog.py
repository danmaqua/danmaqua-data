#!/usr/bin/env python3
# encoding: UTF8
from os import listdir, mkdir
from os.path import isdir, isfile, join, abspath
from shutil import rmtree
import csv
import json

def main():
    group_csv_path = '../raw/groups.csv'
    groups = []
    with open(group_csv_path, mode='r', encoding='utf-8') as f_obj:
        reader = csv.DictReader(f_obj)
        groups.extend(list(reader))

    csv_path = '../raw/vtubers'
    csv_files = [f for f in listdir(csv_path) if isfile(join(csv_path, f))]
    vtubers = []
    for csv_file in csv_files:
        with open(join(csv_path, csv_file), mode='r', encoding='utf-8') as f_obj:
            reader = csv.DictReader(f_obj)
            vtubers.extend(list(reader))

    if len(groups) == 0 or len(vtubers) == 0:
        raise Exception('No groups and vtubers data in raw folders')
    
    output_path = '../room/vtubers'
    rmtree(output_path)
    if not isdir(output_path):
        mkdir(output_path)
    for group in groups:
        group_path = join(output_path, group['name'] + '.json')
        vtubers_in_group = list(filter(
            lambda item: item['group'] == group['name'],
            vtubers
        ))
        group['count'] = len(vtubers_in_group)
        group_obj = {
            'version': 1,
            'name': group['name'],
            'title': group['title'],
            'data': vtubers_in_group
        }
        with open(group_path, mode='w', encoding='utf-8') as f_obj:
            f_obj.write(json.dumps(group_obj, indent=4, ensure_ascii=False))
    catalog_obj = {
        'version': 1,
        'data': groups
    }
    with open('../room/vtubers_catalog.json', mode='w', encoding='utf-8') as f_obj:
        f_obj.write(json.dumps(catalog_obj, indent=4, ensure_ascii=False))
    print('Done')

if __name__ == '__main__':
    main()
