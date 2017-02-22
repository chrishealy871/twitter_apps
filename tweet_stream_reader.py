import json
import pandas
import matplotlib.pyplot as plt
from api_keys import get_auth

tweets_data_path = 'tweet_mining.json'

results = []
tweets_file = open(tweets_data_path)
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue

print len(results)