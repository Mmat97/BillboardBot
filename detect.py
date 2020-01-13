import tweepy

print("twiiter bot")

CONSUMER_KEY='B7sHr2ftDRvSVauPpTxBYCzNd'
CONSUMER_SECRET='9Nu6TlVDbuRqNh3ud4APQnxJy4zMlBfpOG2I2u7hJMSuqDnMcq'


ACCESS_KEY='1109979573104594944-Z9tex9jutg5HGPHaj4aejsqa79pcFK'
ACCESS_SECRET='fYg0GmKVJqsPJ0Q34b9imMYOhzNcjO6jKf0NQsFHcDfvR'

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api=tweepy.API(auth)

print(api)
print(api.mentions_timeline())
