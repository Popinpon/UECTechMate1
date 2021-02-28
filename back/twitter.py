import tweepy
import requests
import json
import setting
from websocket import create_connection
from utils.logConf import logging
import time
import calendar
logger = logging.getLogger(__name__)

keyword1 = 'ポケモン'
keyword2 = 'エヴァ'
keyword3 = 'TOEIC'

query_keywords = keyword1 + ',' + keyword2 + ',' + keyword3


def utc_to_jst(created_at):
    time_utc = time.strptime(created_at, '%Y-%m-%d %H:%M:%S')
    unix_time = calendar.timegm(time_utc)
    time_local = time.localtime(unix_time)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_local)


class Listener(tweepy.StreamListener):
    def on_status(self, status):
        ws = create_connection(setting.WEBSOCKET_SERVER_URL)
        room_type = ''
        if keyword1 in status.text:
            room_type = 'A'
        elif keyword2 in status.text:
            room_type = 'B'
        elif keyword3 in status.text:
            room_type = 'C'

        if room_type == '':
            return True
        created_at = utc_to_jst(str(status.created_at))
        data = json.dumps(
            {'type': 'twitter', 'room_type': room_type, 'icon_url': status.user.profile_image_url, 'id': status.id, 'user': status.user.name, 'user_id': status.user.screen_name, 'created_at': str(created_at), 'text': status.text})
        ws.send(data)
        logger.debug(data+'\n')
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
    stream.filter(track=[query_keywords])
