import tweepy
import setting


class Listener(tweepy.StreamListener):
    def on_status(self, status):
        status.text()
        # なんかやる
        print('--------------------------------')
        print(status.text)
        print("")
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
    print(COMSUMER_KEY)
    print(COMSUMER_KEY_SECRET)
    print(ACCESS_TOKEN_KEY)
    print(ACCESS_TOKEN_KEY_SECRET)

    auth = tweepy.OAuthHandler(COMSUMER_KEY, COMSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_KEY_SECRET)

    listener = Listener()
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['#技育祭', '#Room'])

    # api = tweepy.API(auth, wait_on_rate_limit=True)

    # data = []
    # for tweet in tweepy.Cursor(api.search, q='#RoomA', count=10).items():
    #     tweet_data = [tweet.created_at, tweet.user.id_str, tweet.text]
    #     data.append(tweet_data)

    # print(data)

    # tweets = api.search(q='#RoomA', lang='ja',
    #                     result_type='recent', count=10)
