import json
import os

from cloudant import Cloudant
from flask import Flask, redirect, url_for, request, jsonify
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.settings import Settings

from startrek import settings as my_settings
from startrek.spiders.starTrek_spider import starTrekSpider

app = Flask(__name__, static_url_path='')

port = int(os.getenv('PORT', 8000))

app = Flask(__name__, static_url_path='')

db_name = 'webscrapingteste'
client = None
db = None

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/get_data', methods=['GET'])
def search():
    # craw e gera JSON
    configure_logging()
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    runner = CrawlerRunner(settings=crawler_settings)
    runner.crawl(starTrekSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    #redirect(url_for('save_data'))


@app.route('/save_data', methods=['POST'])
def save_data():
    if client:
        with open('startrek.json') as f:
            for url in f:
                data = json.loads(url)
                my_document = db.create_document(data)
                data['_id'] = my_document['_id']
        # Close opend file
        f.close()
        return jsonify(data)
    else:
        return ('No database')


@app.route('/return_data', methods=['GET'])
def return_data():
    if client:
        return jsonify(list(map(lambda doc: doc['url'], db)))
    else:
        print('No database')
        return jsonify([])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
