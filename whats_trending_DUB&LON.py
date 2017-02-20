import json

from api_keys import twitter_api
api = twitter_api()

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)


print json.dumps(dub_trends, indent=1)
print json.dumps(lon_trends, indent=1)