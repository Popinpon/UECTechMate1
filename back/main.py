from flask import Flask, render_template, request, jsonify
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import os
import json
import time
import datetime

app = Flask(__name__, static_folder='../dist/static',
            template_folder='../dist')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
