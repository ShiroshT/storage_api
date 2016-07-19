import os
import sqlite3
from TwitterSearch import *
from settings import *
import time
from database_create import *
from database_open_close import *

'''Commit Source list to the database.'''


def commit_source_master(c, conn, data_sources):
    length = len(data_sources['sources'])

    try:
        for i in xrange(length):
            news_source_id = data_sources['sources'][i]['id']
            news_source_name = data_sources['sources'][i]['name']
            news_source_desc = data_sources['sources'][i]['description']
            news_source_url = data_sources['sources'][i]['url']
            news_source_sort = data_sources['sources'][i]['sortBysAvailable'][0]
            c.execute("insert into source_master values (?, ?,?,?,?)",
                      (news_source_id, news_source_name, news_source_desc, news_source_url, news_source_sort))
    except:
        print 'unique contraints are not met - news_source_id is a primary key'

        # close(c)


''' Commit full load master to the data base'''


def commit_full_load_master(c, conn, data_sources):
    length = len(data_sources['articles'])
    for i in xrange(length):
        try:
            tempval1 = data_sources['source'] + data_sources['articles'][i]['title']
            tempval2 = tempval1.replace(" ", "")[0:35]

            fload_id = tempval2
            fload_status = data_sources['status']
            fload_source = data_sources['source']
            fload_author = data_sources['articles'][i]['author']
            fload_description = data_sources['articles'][i]['description']
            fload_title = data_sources['articles'][i]['title']
            fload_url = data_sources['articles'][i]['url']
            fload_urltoimage = data_sources['articles'][i]['urlToImage']
            fload_publishedAt = data_sources['articles'][i]['publishedAt']
            c.execute("insert into news_loadfull_master values (?, ?,?,?,?,?,?,?,?)",
                      (fload_id, fload_status, fload_source, fload_author, fload_description, fload_title,
                       fload_url, fload_urltoimage, fload_publishedAt))
            print fload_status
            print fload_title

        except:
            print 'The write has not been completed for',i, 'the news story already available'
        conn.commit()
















# dbflag_master= 0
# dbflag_tw = 0
# dbflag_master = createDatabase_master(c, conn, dbflag_master)
# dbflag_tw = createDatabase_twitter(c, conn,dbflag_tw)
#
#
# commit_master_news(c, conn, table_name_master, dataexport, dbflag_master)
# twitter_feed_search(c, conn, table_name_master,table_name_twitter,dbflag_tw)
# close(conn)





#
# def commit_master_news(c, conn, table_name, dataexport, dbflag_master):
#     print 'writing from Guardian '
#
#     les = len(dataexport['response']['results'])
#
#     maxid = 0
#
#     if dbflag_master == 1:
#         maxid = 0
#         p = c.execute('SELECT max(mnewsitemID) FROM {}'.format(table_name))
#         maxid = p.fetchone()[0]
#         maxid = maxid + 1
#
#     for i in xrange(les):
#         valf = i
#         title_a = dataexport['response']['results'][i]['fields']['headline']
#         url_a = dataexport['response']['results'][i]['webUrl']
#         section_a = dataexport['response']['results'][i]['sectionName']
#         webtit_a = dataexport['response']['results'][i]['webTitle']
#         link_a = dataexport['response']['results'][i]['fields']['shortUrl']
#         main_a = dataexport['response']['results'][i]['fields']['main']
#         body_a = dataexport['response']['results'][i]['fields']['body']
#
#         c.execute("insert into news_store_master values (?, ?,?,?,?,?,?,?)",
#                   (valf + maxid, title_a, url_a, section_a, webtit_a, link_a, main_a, body_a))
#
#
# ''' Assign values to the database from the API - Twitter from the values got from the Guardian'''
#
#
# def twitter_feed_search(c, conn, table_name_master, table_name_twitter, dbflag_tw):
#     print 'going to twitter'
#     p = c.execute('SELECT title FROM {}'.format(table_name_master))
#     allresult = p.fetchall()
#     p_count = c.execute('SELECT count(mnewsitemID) FROM {}'.format(table_name_master))
#     p_count_i = p_count.fetchone()[0]
#
#     for i in xrange(p_count_i):
#
#         title = allresult[i][0]
#         titlelist = []
#         titlelist.append(title)
#
#         try:
#             tso = TwitterSearchOrder()
#             tso.set_keywords(titlelist)
#             ts = TwitterSearch(
#                 consumer_key=twitter_consumer_key,
#                 consumer_secret=twitter_consumer_secret,
#                 access_token=twitter_access_token,
#                 access_token_secret=twitter_access_token_secret
#             )
#             sleep_for = 60  # sleep for 60 seconds
#             last_amount_of_queries = 0  # used to detect when new queries are done
#
#             for tweet in ts.search_tweets_iterable(tso):
#                 print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))
#                 current_amount_of_queries = ts.get_statistics()[0]
#                 if not last_amount_of_queries == current_amount_of_queries:
#                     last_amount_of_queries = current_amount_of_queries
#                     time.sleep(sleep_for)
#
#         except TwitterSearchException as e:
#             print(e)
#
# ''' Assign values to the database from the NEWS API - source list'''
