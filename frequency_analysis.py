import json

from api_keys import twitter_api
import tweepy
from tweepy import OAuthHandler
from collections import Counter
api = twitter_api()

count = 50
query = 'Trump'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions']]

hashtags = [hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags']]

words = [w for t in status_texts
         for w in t.split()]

for entry in [screen_names, hashtags, words]:
    counter = Counter(entry)
    print counter.most_common()[:10]  # the top 10 results
    print