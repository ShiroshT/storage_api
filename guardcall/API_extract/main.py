import os
from storage.model_tab import *
from storage.data_extract import *
from storage.database_create import *
from apicall.guadcall import *






''' create database source master - in database_create.py'''
c, conn =db_create_source_master()
data_sources = examine_sources()
commit_source_master(c, conn, data_sources)
close(c)



'''extract data from each source -'''
c, conn = db_create_full_load()
data_pulled = data_extract_from_source(c, conn)
# close(c)







# exportData = get_content()


# print 'about to create database'
# databasepost(exportData)
