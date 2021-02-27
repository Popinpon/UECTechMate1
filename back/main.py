from flask import Flask, render_template, request, jsonify
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import os
import json
import time
import base64
import datetime

app = Flask(__name__, static_folder='../dist/static',
            template_folder='../dist')


@app.route('/get_schedule_json', methods=['POST'])
def get_schedule():
    data = ""
    with open('./data/schedule.json', 'r', encoding="utf-8_sig") as f:
        data = json.load(f)
    return jsonify({"json_data": data})


@app.route('/save_img', methods=['POST'])
def save_img():
    data = request.data.decode('utf-8')
    data_json = json.loads(data)
    image = data_json['image']
    image_dec = base64.b64decode(image)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
