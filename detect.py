import tweepy

print("twiiter bot")

CONSUMER_KEY='B7sHr2ftDRvSVauPpTxBYCzNd'
CONSUMER_SECRET='9Nu6TlVDbuRqNh3ud4APQnxJy4zMlBfpOG2I2u7hJMSuqDnMcq'

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api=tweepy.API(auth)