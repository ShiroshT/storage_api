from TwitterSearch import *
from setting import *

import time


try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['foo', 'bar'])
    
    ts = TwitterSearch(
                       consumer_key = 'aaabbb',
                       consumer_secret = 'cccddd',
                       access_token = '111222',
                       access_token_secret = '333444'
                       )
    sleep_for = 60 # sleep for 60 seconds
    last_amount_of_queries = 0 # used to detect when new queries are done
                       
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        current_amount_of_queries = ts.get_statistics()[0]
        if not last_amount_of_queries == current_amount_of_queries:
            last_amount_of_queries = current_amount_of_queries
            time.sleep(sleep_for)



except TwitterSearchException as e:
    print(e)