import tweepy
import time
from api_keys import APISecrets

# create a file called api_keys.py and enter the below in that
# from enum import Enum

# class APISecrets(Enum):
#     CONSUMER_SECRET = "your consumer secret"
#     CONSUMER_KEY = "your consumer key"
#     ACCESS_TOKEN = "your access tokem"
#     ACCESS_SECRET = "your access secret"

auth = tweepy.OAuthHandler(APISecrets.CONSUMER_KEY.value, APISecrets.CONSUMER_SECRET.value)
auth.set_access_token(APISecrets.ACCESS_TOKEN.value, APISecrets.ACCESS_SECRET.value)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
user = api.me()
print(user.name, user.followers_count)
# for tweet in public_tweets:
#     print(tweet.text)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)
    except StopIteration:
        exit()

# Generous bot
# the wrapping of cursor with limit_handler ensures that 
# if we hit the rate limit for the api, the script pauses
# for a second and then continues; instead of throwing errors and coming to a halt
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.followers_count > 10:
#         follower.follow()
#         break

search_string = "python tip"
number_of_tweets = 4

for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    try:
        print( tweet.text)
    except tweepy.TweepError as error:
        print(err.reason)
    except StopIteration:
        break
