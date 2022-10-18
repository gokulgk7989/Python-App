from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return '<h1 style="color:red">Welcome to Demo python app</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
