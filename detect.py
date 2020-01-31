import tweepy
from bch1 import billboard

#pip3 isnat python-twooter

CONSUMER_KEY='B7sHr2ftDRvSVauPpTxBYCzNd'
CONSUMER_SECRET='9Nu6TlVDbuRqNh3ud4APQnxJy4zMlBfpOG2I2u7hJMSuqDnMcq'
ACCESS_KEY='1109979573104594944-Z9tex9jutg5HGPHaj4aejsqa79pcFK'
ACCESS_SECRET='fYg0GmKVJqsPJ0Q34b9imMYOhzNcjO6jKf0NQsFHcDfvR'

def getAPI(ck,cs,ak,am):
    auth=tweepy.OAuthHandler(ck,cs)
    auth.set_access_token(ak, am)
    api=tweepy.API(auth)
    return api

api=getAPI(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

def postStats():
    chart = billboard.ChartData('hot-100')
    try:
        api.update_status("Top Song Right Now: " + str(chart[0]))
    except tweepy.TweepError as error:
        if error.api_code == 187:
            print('duplicate message')
        else:
            raise error
    #update_status('Updating using OAuth authentication via Tweepy!')




postStats()