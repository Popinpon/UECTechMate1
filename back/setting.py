import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__)+'.env')
load_dotenv(dotenv_path)

CSKEY = os.environ.get("consumer_key")
CSKEY_SEC = os.environ.get("consumer_secret")
TKNKEY = os.environ.get("access_token_key")
TKNKEY_SEC = os.environ.get("access_token_secret")
YT_API_KEY = os.environ.get("youtube_api_key")
WEBSOCKET_SERVER_URL = "ws://localhost:5001"
YT_URL={"RoomA":"https://www.youtube.com/watch?v=coYw-eVU0Ks"}#, "RoomB":"b url", "RoomC":"c url"}
