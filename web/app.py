import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis_1", port=6379)

@app.route('/')
def hello():
    redis.incr('views')
    return '<p id="views">Hello! This page has been seen {0} times.</p>'.format(
        redis.get('views').decode('utf-8'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
