import json

from api_keys import twitter_api
api = twitter_api()

DUB_WOE_ID = 560743

dub_trends = api.trends_place(DUB_WOE_ID)

print json.dumps(dub_trends, indent=1)