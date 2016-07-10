import os

from storage.model_tab import comitetoDatabase
from storage.model_tab import databasepost
from apicall.guadcall import get_content


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
exportData = get_content()

print 'about to create database'
databasepost(exportData)

#exportData['response']['results'][1]['fields']['body']
