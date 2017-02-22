from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from api_keys import get_auth



keyword_list = ['Ireland', 'France', 'Italy']  # track list
limit = 500


class MyStreamListener(StreamListener):

    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                with open('tweet_mining.json', 'a') as tweet_file:
                    tweet_file.write(data)
                    return True
            except BaseException as e:
                print "Failed on_data: %s" % str(e)
            return True
        else:
         return False

    def on_error(self, status):
        print status
        return True


twitter_stream = Stream(get_auth(), MyStreamListener())
twitter_stream.filter(track=keyword_list)