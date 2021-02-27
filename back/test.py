import requests
from PIL import Image
import json
import base64
from io import BytesIO
import os

# /save_imgに画像送るテスト

img = Image.open(os.path.abspath('../dist/static/img/no_image.jpg'))

buffered = BytesIO()
img.save(buffered, format="JPEG")
img_byte = buffered.getvalue()
img_base64 = base64.b64encode(img_byte)

img_str = img_base64.decode('utf-8')
json_data = {
    "room_type": "A",
    "img": img_str
}
r = requests.post("http://127.0.0.1:5000/save_img",
                  json=json.dumps(json_data))
print(r.json())
