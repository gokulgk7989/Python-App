from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return '<h1 style="color:green">Welcome to Demo python app -version-2.0.1</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
