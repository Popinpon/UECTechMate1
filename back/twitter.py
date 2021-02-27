import tweepy
import requests
import json
import setting
from websocket import create_connection
import logging

logger = logging.getLogger(__name__)


class Listener(tweepy.StreamListener):
    def on_status(self, status):
        logger.debug('----------------------')
        logger.debug(status+'\n')
        ws = create_connection("ws://localhost:5001")
        ws.send(json.dumps(
            {'type': 'twitter', 'id': status.id, 'user': status.user.name, 'user_id': status.user.screen_name, 'created_at': str(status.created_at), 'text': status.text}))
        result = ws.recv()
        ws.close()
        return True

    def on_error(self, status_code):
        print('Got an error with status code: '+str(status_code))
        return False

    def on_timeout(self):
        print('Timeout...')
        return False


if __name__ == '__main__':
    COMSUMER_KEY = setting.CSKEY
    COMSUMER_KEY_SECRET = setting.CSKEY_SEC
    ACCESS_TOKEN_KEY = setting.TKNKEY
    ACCESS_TOKEN_KEY_SECRET = setting.TKNKEY_SEC

    auth = tweepy.OAuthHandler(COMSUMER_KEY, COMSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_KEY_SECRET)

    listener = Listener()
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['アルセウス'])
