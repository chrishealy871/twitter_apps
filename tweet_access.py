import json

from api_keys import twitter_api
import tweepy
api = twitter_api()

count = 10
query = 'Dublin'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
    print result