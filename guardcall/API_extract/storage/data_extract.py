import os
import sqlite3
from TwitterSearch import *
from settings import *
import time
from database_create import *
from database_open_close import *
from data_commit import *
import urlparse
import requests



def data_extract_from_source(c,conn):
    conn, c, table_name_master, table_name_twitter, table_name_source = database_open()
    p = c.execute('SELECT news_source_id  FROM {}'.format(table_name_source))
    allresult = p.fetchall()
    source_len = len(allresult)
    newsapi_key = 'eef3c6b4b7c34067aca9af92c53e4da0'

    base_url = 'https://newsapi.org/v1/'
    sleep_for = 60
    for i in xrange(source_len):
        url_comp1 = 'articles?source=' +allresult[i][0] + '&apiKey=eef3c6b4b7c34067aca9af92c53e4da0'
        url_api =urlparse.urljoin(base_url,  url_comp1)
        response = requests.get(url_api)
        data = response.json()  # convert json to python-readable format
        commit_full_load_master(c, conn, data)
        time.sleep(sleep_for)



