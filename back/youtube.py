# https://qiita.com/iroiro_bot/items/ad0f3901a2336fe48e8f
import time
import requests
import json
import datetime
import dateutil.parser
import setting
from websocket import create_connection

def get_chat_id(room_type):

    '''
    https://developers.google.com/youtube/v3/docs/videos/list?hl=ja
    '''
    video_id = setting.YT_URL[room_type].replace('https://www.youtube.com/watch?v=', '')
    print('video_id : ', video_id)

    url = 'https://www.googleapis.com/youtube/v3/videos'
    params = {'key': setting.YT_API_KEY, 'id': video_id,
              'part': 'liveStreamingDetails'}
    data = requests.get(url, params=params).json()

    liveStreamingDetails = data['items'][0]['liveStreamingDetails']
    if 'activeLiveChatId' in liveStreamingDetails.keys():
        chat_id = liveStreamingDetails['activeLiveChatId']
        print('get_chat_id done!')
        currViewrs = liveStreamingDetails['concurrentViewers']
        viewerstext = '[{} viewrs]\n'.format(currViewrs)
        print(viewerstext)
    else:
        chat_id = None
        print('NOT live')

    return chat_id


def get_chat(room,chat_id, pageToken):
    '''
    https://developers.google.com/youtube/v3/live/docs/liveChatMessages/list
    '''
    url = 'https://www.googleapis.com/youtube/v3/liveChat/messages'

    params = {'key': setting.YT_API_KEY, 'liveChatId': chat_id,'part': 'id,snippet,authorDetails'} #コメント主のチャンネル詳細
    if type(pageToken) == str:
        params['pageToken'] = pageToken

    data = requests.get(url, params=params).json()

    if len(data['items']) > 0:
        try:
            for i,item in enumerate(data['items']):

                channelId = item['snippet']['authorChannelId']
                msg = item['snippet']['displayMessage']
                usr       = item['authorDetails']['displayName']#コメント主名
                icon = item['authorDetails']['profileImageUrl']
                # supChat   = item['snippet']['superChatDetails']#スパチャ
                #supStic   = item['snippet']['superStickerDetails']

                # with open(log_file, 'a') as f:
                #     print(log_text, file=f)
                #     print(log_text)

                JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')  # ISO表記のUTCー＞JSTへ
                at= data['items'][i]['snippet']['publishedAt']
                at = dateutil.parser.parse(at).astimezone(JST)
                at = "{0:%Y-%m-%d %H:%M:%S}".format(at)

                ws = create_connection("ws://localhost:5001")
                jmsg=json.dumps({'type': 'youtube','room_type':room, 'id':" ",'user':usr ,'user_id':channelId , 'created_at': str(at), 'text': msg,'icon':icon})

                ws.send(jmsg)
                result = ws.recv()
                ws.close()
                print(jmsg)

        except Exception as e:
            print(e+"err!")
    else:
        print("no comments")

    return data['nextPageToken']


def main():
    slp_time = 10  # sec
    iter_times = 5  # 回
    take_time = slp_time / 60 * iter_times
    room_names=list(setting.YT_URL)

    chat_ids=[]
    nextPageToken=[]
#    log_file = yt_url.replace('https://www.youtube.com/watch?v=', '') + '.txt'
    for i,room in enumerate(room_names):
        chat_ids.append(get_chat_id(room))
        nextPageToken.append(None)

    for ii in range(iter_times):
        # for jj in [0]:
        for i,chat_id in enumerate(chat_ids):
            try:
                print('\n')
                nextPageToken[i] = get_chat(room_names[i],chat_id, nextPageToken[i])
                time.sleep(slp_time)
            except Exception as e:
                print(e)

if __name__ == '__main__':

    main()
