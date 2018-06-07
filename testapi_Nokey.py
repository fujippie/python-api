import json
from requests_oauthlib import OAuth1Session
from time import sleep
#CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET) #認証処理

def userTimeline():
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント
    params ={'count' : 5} #取得数
    res = twitter.get(url, params = params)

    if res.status_code == 200: #正常通信出来た場合
        timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
        for line in timelines: #タイムラインリストをループ処理
            print('id:' + str(line['id']))
            print(line['user']['name']+'::'+line['text'])
            print(line['created_at'])

            print('*******************************************')
    else: #正常通信出来なかった場合
        print("Failed: %d" % res.status_code)
    return res.status_code

def postTweet():
    tweetId = ''
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {'status':'APIテスト'}
    res = twitter.post(url,params = params)
    if res.status_code == 200:
        tweet = json.loads(res.text)
        tweetId = str(tweet['id'])
    else :
        print("tweetFail" + str(res.status_code ))
    print(tweetId)

    return tweetId

def deleteTweet( tweetId ):

    if not tweetId:
        return False

    sleep(20)

    url = "https://api.twitter.com/1.1/statuses/destroy/"+ tweetId + ".json"
    params = {'id',tweetId}
    res = twitter.post(url)
    if res.status_code == 200:
        return True
    else :
        print("delete fail" + str(res.status_code ))
        return False

deleteTweet(postTweet())
#print(userTimeline())
