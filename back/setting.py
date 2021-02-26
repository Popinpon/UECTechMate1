import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__)+'.env')
load_dotenv(dotenv_path)

CSKEY = os.environ.get("consumer_key")
CSKEY_SEC = os.environ.get("comsumer_secret")
TKNKEY = os.environ.get("access_token_key")
TKNKEY_SEC = os.environ.get("access_token_secret")
