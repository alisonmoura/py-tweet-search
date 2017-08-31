import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
 
consumer_key = 'yIczbjmOZNv6I6p8F1uOfyGK3'
consumer_secret = 'kmyV3JVgkyeq3oOlDf8njSE84k97TYPqHZolUqy5YenXBOKSTq'
access_token = '2267750412-CKai4FIDEipaG2UJXwlbNYhQzOOfTgFdsuhJtQo'
access_secret = 'vJwHwdSaC8U8qwa568PtGDIlkyr265gvsTDLiIsd6kail'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

 
class HashTagListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, HashTagListener())
twitter_stream.filter(track=['#python'])