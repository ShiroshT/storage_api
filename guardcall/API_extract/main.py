import os
from storage.data_commit import *
from storage.data_extract import *
from storage.database_create import *
from crawling.extract_link_from_db import *
from apicall.guadcall import *

''' create database source master - in database_create.py'''
# c, conn = db_create_source_master()
# data_sources = examine_sources()
# commit_source_master(c, conn, data_sources)
# close(c)

'''extract data from each source -'''
# c, conn = db_create_full_load()
# data_pulled = data_extract_from_source(c, conn)
# close(c)

''' start Crawler'''
conn, c, table_name_master, table_name_twitter, table_name_source = database_open()
extract_data_frommaster(conn,c,)











# exportData = get_content()


# print 'about to create database'
# databasepost(exportData)
