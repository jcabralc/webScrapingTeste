# -*- coding: utf-8 -*-

# Scrapy settings for the project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
'''
BOT_NAME = 'starTrek'

SPIDER_MODULES = ['startrek.spiders']
NEWSPIDER_MODULE = 'startrek.spiders'

DOWNLOAD_DELAY = .25
RANDOMIZE_DOWNLOAD_DELAY = True

SPIDER_SETTINGS = [
    {
        'endpoint': 'starTrek',
        'location': 'startrek.spiders.starTrek_spider',
        'spider': 'starTrek',
    }
]
'''

ITEM_PIPELINES = {
    'startrek.pipelines.JsonWithEncodingPipeline': 300,
    'startrek.pipelines.CloudantPipeline': 500,
}

'''
SPIDER_SETTINGS = [
    {
        'endpoint': 'starTrek',
        'location': 'spiders.starTrek_spider',
        'spider': 'starTrek_spider',
    }
]
'''