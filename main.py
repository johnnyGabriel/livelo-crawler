from flask import Flask
from livelocrawler.crawler import LiveloCrawler
from redis import Redis

api = Flask(__name__)
redis = Redis(host='localhost', port=6379, decode_responses=True)
crawler = LiveloCrawler()

# getting data from crawler
partners = crawler.get_partners_data()
partners_dict = dict(zip(partners['Partner'], partners['Score']))

# redis saving
redis.hset('partners', mapping=partners_dict)
redis.expire('partners', 100)

# api handler
@api.route('/')
def hello_world():
    return '<p>Hello World</p>'


