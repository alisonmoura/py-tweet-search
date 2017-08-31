import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'yIczbjmOZNv6I6p8F1uOfyGK3'
consumer_secret = 'kmyV3JVgkyeq3oOlDf8njSE84k97TYPqHZolUqy5YenXBOKSTq'
access_token = '2267750412-CKai4FIDEipaG2UJXwlbNYhQzOOfTgFdsuhJtQo'
access_secret = 'vJwHwdSaC8U8qwa568PtGDIlkyr265gvsTDLiIsd6kail'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status._json)

for friend in tweepy.Cursor(api.friends).items(10):
    # Process a single status
    print(friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items():
    print(tweet._json)