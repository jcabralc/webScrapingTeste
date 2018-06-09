# -*- coding: utf-8 -*-

from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
import os
import json
from scrapy.exceptions import DropItem
import json
import codecs

class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('startrek.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
        print('JSON GERADO!')


class CloudantPipeline(object):

    def process_item(self, item, spider):
        return item