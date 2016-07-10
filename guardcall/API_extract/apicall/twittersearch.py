from TwitterSearch import *
from settings import *
import time


try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['brexit', 'May'])
    
    ts = TwitterSearch(
                       consumer_key = twitter_consumer_key,
                       consumer_secret = twitter_consumer_secret,
                       access_token = twitter_access_token,
                       access_token_secret = twitter_access_token_secret
                       )
    sleep_for = 5 # sleep for 60 seconds
    last_amount_of_queries = 0 # used to detect when new queries are done
    
    for tweet in ts.search_tweets_iterable(tso):
        print tweet
#        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        current_amount_of_queries = ts.get_statistics()[0]
        if not last_amount_of_queries == current_amount_of_queries:
            last_amount_of_queries = current_amount_of_queries
            time.sleep(sleep_for)



except TwitterSearchException as e:
    print(e)