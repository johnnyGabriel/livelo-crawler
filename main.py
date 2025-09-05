from flask import Flask
from livelocrawler.crawler import LiveloCrawler
from redis import Redis
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HASH = 'partners'

api = Flask(__name__)
redis = Redis(
    host=os.environ.get('REDIS_HOST'), 
    port=os.getenv('REDIS_PORT'), 
    decode_responses=True)
crawler = LiveloCrawler()

def get_partners():
    partners = redis.hgetall(REDIS_HASH)
    if partners == {}:
        partners = crawler.get_partners_data()
        partners = dict(zip(partners['Partner'], partners['Score']))
        redis.hset(REDIS_HASH, mapping=partners)
        redis.expire(REDIS_HASH, os.getenv('REDIS_CACHE_EXP_MIN'))
    return partners

def transform_to_response(partners: dict):
    res = []
    for partner_name, score in partners.items():
        res.append({
            'partner_name': partner_name,
            'score': score
        })
    return res

# api handler
# run: flask --app main run
@api.route('/')
def get_all_partners():
    try:
        partners = get_partners()
        return transform_to_response(partners)
    except:
        api.logger.error('error getting partners', exc_info=True)
        return 'Internal Server Error', 500

if __name__ == "__main__":
    api.run(
        host=os.getenv('FLASK_RUN_HOST'), 
        port=os.getenv('FLASK_RUN_PORT'), 
        debug=True)