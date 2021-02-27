import tweepy
import requests
import json
import setting
from websocket import create_connection


class Listener(tweepy.StreamListener):
    def on_status(self, status):
        print('----------------------')
        print(status.text)
        print("")
        ws = create_connection("ws://localhost:5001")
        ws.send(json.dumps(
            {'type': 'twitter', 'id': status.id, 'created_at': str(status.created_at), 'text': status.text}))
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

    # api = tweepy.API(auth, wait_on_rate_limit=True)

    # data = []
    # for tweet in tweepy.Cursor(api.search, q='#RoomA', count=10).items():
    #     tweet_data = [tweet.created_at, tweet.user.id_str, tweet.text]
    #     data.append(tweet_data)

    # print(data)

    # tweets = api.search(q='#RoomA', lang='ja',
    #                     result_type='recent', count=10)
