import os
import sqlite3
from TwitterSearch import *
from settings import *
import time

''' Connect to database '''
def connect(sqlite_file):
    """ Make connection to an SQLite database file """
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return conn, c

''' Close database '''
def close(conn):
    """ Commit changes and close connection to the database """
    conn.commit()
    conn.close()



''' Create databases - news_store_master, twitter_store '''
def createDatabase_twitter(c, conn):
    try:
        conn.execute('''  CREATE TABLE twitter_store(
            twitter_id    TEXT,
            text   TEXT,
            userid TEXT,
            master_newsid REFERENCES news_store_master(mnewsitemID));''')
        
        print "Table created successfully";
        

    
    except sqlite3.Error as er:
        print 'database already availble:', er.message
        dbcreateflag = 1



''' Create databases - news_store_master, twitter_store '''
def createDatabase_master(c, conn):
    try:
        
        conn.execute('''CREATE TABLE news_store_master
            (mnewsitemID INT PRIMARY KEY     NOT NULL,
            title           TEXT    NOT NULL,
            urllink         TEXT     NOT NULL,
            section         TEXT ,
            webtitle        TEXT NOT NULL,
            link            TEXT NOT NULL,
            main            TEXT NOT NULL,
            body            TEXT NOT NULL);''')
        
        conn.execute('''  CREATE TABLE twitter_store(
            twitter_id    TEXT,
            text   TEXT,
            userid TEXT,
            FOREIGN KEY (master_newsid) REFERENCES news_store_master(mnewsitemID));''')
        
        print "Table created successfully";
        
        conn.close()
        dbcreateflag = 0
    
    except sqlite3.Error as er:
        print 'database already availble:', er.message
        dbcreateflag = 1


    print 'dbflag',dbcreateflag
    return dbcreateflag



''' Assign values to the database from the API - Guardian'''

def commit_master_news(c, conn, table_name, dataexport,dbcreateflag):

    les = len(dataexport['response']['results'])
    
    maxid = 0

#    if dbcreateflag ==1:
#        maxid = 0
#        p = c.execute('SELECT max(mnewsitemID) FROM {}'.format(table_name))
#        maxid = p.fetchone()[0]
#        maxid = maxid +1

    for i in xrange(les):
        valf = i
        title_a = dataexport['response']['results'][i]['fields']['headline']
        url_a = dataexport['response']['results'][i]['webUrl']
        section_a = dataexport['response']['results'][i]['sectionName']
        webtit_a = dataexport['response']['results'][i]['webTitle']
        link_a = dataexport['response']['results'][i]['fields']['shortUrl']
        main_a = dataexport['response']['results'][i]['fields']['main']
        body_a = dataexport['response']['results'][i]['fields']['body']
        
        c.execute("insert into news_store_master values (?, ?,?,?,?,?,?,?)", (valf + maxid, title_a, url_a, section_a, webtit_a, link_a, main_a,body_a))


''' Assign values to the database from the API - Twitter from the values got from the Guardian'''


def twitter_feed_search(c, conn, table_name_master,table_name_twitter):
    p = c.execute('SELECT title FROM {}'.format(table_name_master))
    allresult = p.fetchall()
    p_count = c.execute('SELECT count(mnewsitemID) FROM {}'.format(table_name_master))
    p_count_i = p_count.fetchone()[0]
    
    for i in xrange(p_count_i):
        
        title=allresult[i][0]
        titlelist=[]
        titlelist.append(title)
        
        try:
            tso = TwitterSearchOrder()
            print 'titlelistquery',titlelist
            tso.set_keywords(titlelist)
            ts = TwitterSearch(
                               consumer_key = twitter_consumer_key,
                               consumer_secret = twitter_consumer_secret,
                               access_token = twitter_access_token,
                               access_token_secret = twitter_access_token_secret
                               )
            sleep_for = 60  # sleep for 60 seconds
            last_amount_of_queries = 0 # used to detect when new queries are done
                               
                               
            for tweet in ts.search_tweets_iterable(tso):
                print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
                current_amount_of_queries = ts.get_statistics()[0]
                if not last_amount_of_queries == current_amount_of_queries:
                        last_amount_of_queries = current_amount_of_queries
                        time.sleep(sleep_for)
  
  
##write to database
#            p = c.execute('SELECT max(mnewsitemID) FROM {}'.format(table_name))
#            maxid = p.fetchone()[0]
#            maxid = maxid +1


        except TwitterSearchException as e:
            print(e)




def databasepost(dataexport):
    sqlite_file = '/Users/siyanetissera/development/scratch_space/API_test/guardcall/API_extract/APIStorage.sqlite'
    table_name_master = 'news_store_master'
    table_name_twitter = 'twitter_store'
    conn, c = connect(sqlite_file)
    dbcreateflag = createDatabase_master(c, conn)
    createDatabase_twitter(c, conn)
    
    commit_master_news(c, conn, table_name_master, dataexport,dbcreateflag)
    twitter_feed_search(c, conn, table_name_master,table_name_twitter)
    close(conn)

