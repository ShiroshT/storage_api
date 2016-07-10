import os
import sqlite3


def connect(sqlite_file):
    """ Make connection to an SQLite database file """
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return conn, c


def close(conn):
    """ Commit changes and close connection to the database """
    conn.commit()
    conn.close()



def createDatabase_master(c, conn):
    try:
        
        conn.execute('''CREATE TABLE news_store_master
            (mnewsitemID INT PRIMARY KEY     NOT NULL,
            title           TEXT    NOT NULL,
            urllink          TEXT     NOT NULL,
            section         TEXT ,
            webtitle        TEXT NOT NULL,
            link            TEXT NOT NULL,
            main            TEXT NOT NULL,
            body            TEXT NOT NULL);''')
        
        conn.execute('''  CREATE TABLE twitter_store(
            trackid     INTEGER,
            trackname   TEXT,
            trackartist INTEGER,
            resf REFERENCES news_store_master(mnewsitemID));''')
        
        print "Table created successfully";
        
        conn.close()
        dbcreateflag = 0
    
    except sqlite3.Error as er:
        print 'database already availble:', er.message
        dbcreateflag = 1


    print 'dbflag',dbcreateflag
    return dbcreateflag


def commit_master_news(c, conn, table_name, dataexport,dbcreateflag):

    les = len(dataexport['response']['results'])
    
    print dataexport['response']['results']
    
    maxid = 0

    if dbcreateflag ==1:
        maxid = 0
        p = c.execute('SELECT max(mnewsitemID) FROM {}'.format(table_name))
        maxid = p.fetchone()[0]
        maxid = maxid +1

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


def twitter_feed_search():
    






def databasepost(dataexport):
    sqlite_file = '/Users/siyanetissera/development/scratch_space/API_test/guardcall/API_extract/APIStorage.sqlite'
    table_name = 'news_store_master'
    conn, c = connect(sqlite_file)
    dbcreateflag = createDatabase_master(c, conn)
    commit_master_news(c, conn, table_name, dataexport,dbcreateflag)
    close(conn)

