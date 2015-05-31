import os
import logging
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis_1", port=6379)

log = logging.getLogger('werkzeug')
log.setLevel(getattr(logging, os.environ.get('FLASK_LOG_LEVEL', 'NOTSET')))

@app.route('/')
def hello():
    redis.incr('views')
    return 'Hello! This page has been seen {0} times.'.format(
        redis.get('views').decode('utf-8'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
