from api_keys import twitter_api
import tweepy
from tweepy import OAuthHandler
api = twitter_api()

user = api.get_user('@realdonaldtrump')

print user.screen_name
print user.followers_count

for friend in user.friends():
    print friend.screen_name
    print friend.followers_count
