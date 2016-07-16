import os
from storage.model_tab import *
from apicall.guadcall import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

c, conn =db_create_source_master()
data_sources = examine_sources()
commit_source_master(c, conn, data_sources)

# exportData = get_content()


# print 'about to create database'
# databasepost(exportData)
