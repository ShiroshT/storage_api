import os
import sqlite3
from TwitterSearch import *
from settings import *
import time

''' Create databases - this will store name of all the sources '''


def createDatabase_sourcelist(c, conn):
    try:
        conn.execute('''  CREATE TABLE source_master(
            news_source_id    TEXT PRIMARY KEY NOT NULL,
            news_source_name   TEXT,
            news_source_desc TEXT,
            news_source_url TEXT,
            news_source_sort TEXT);''')

        print "Table soure master created successfully";

    except sqlite3.Error as er:
        print 'database source master already availble', er.message
        dbflag_tw = 1


''' Create databases - news_store_master, twitter_store '''


def createDatabase_twitter(c, conn, dbflag_tw):
    try:
        conn.execute('''  CREATE TABLE twitter_store(
            twitter_id    TEXT,
            text   TEXT,
            userid TEXT,
            master_newsid REFERENCES news_store_master(mnewsitemID));''')

        print "Table created successfully";



    except sqlite3.Error as er:
        print 'database already availble:', er.message
        dbflag_tw = 1

    return dbflag_tw


''' Create databases - news_store_master, twitter_store '''


def createDatabase_master(c, conn, dbflag_master):
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

    except sqlite3.Error as er:
        dbflag_master = 1

    return dbflag_master
