from flask import Flask, render_template, request, jsonify
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from PIL import Image
import os
import json
import time
import base64
import datetime
from io import BytesIO

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
    json_data = request.get_json()
    dict_data = json.loads(json_data)
    img = dict_data["img"]
    room_type = dict_data["room_type"]
    img = base64.b64decode(img)
    img = BytesIO(img)
    img = Image.open(img)
    img.save(os.path.abspath('../dist/static/img/')+'/Room'+room_type+'.png')
    img_shape = img.size
    text = dict_data["text"]
    response = {"text": text, "img_shape": img_shape}
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
