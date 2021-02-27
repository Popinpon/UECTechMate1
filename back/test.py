import requests
from PIL import Image
import json
import base64
from io import BytesIO
import os

# /save_imgに画像送るテスト

img = Image.open(os.path.abspath('../dist/static/img/no_image.jpg'))

# PillowImageをbytesに変換してさらにbase64に変換
buffered = BytesIO()
img.save(buffered, format="JPEG")
img_byte = buffered.getvalue()  # bytes
img_base64 = base64.b64encode(img_byte)  # base64でエンコードされたbytes ※strではない

# まだbytesなのでjson.dumpsするためにstrに変換(jsonの要素はbytes型に対応していないため)
img_str = img_base64.decode('utf-8')  # str
files = {
    "text": "hogehoge",
    "room_type": "A",
    "img": img_str
}
r = requests.post("http://127.0.0.1:5000/save_img",
                  json=json.dumps(files))  # jsonとしてサーバーにPOSTする
print(r.json())
