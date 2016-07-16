import requests
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_content():
    api_url = 'http://content.guardianapis.com/search?q=europe'
    payload = {
        'api-key':              'e76429ae-ad89-497f-a228-abb82b62b9f4',
        'page-size':            10,
        'show-editors-picks':   'true',
        'show-elements':        'image',
        'show-fields':          'all'
    }
    response = requests.get(api_url, params=payload)
    data = response.json() # convert json to python-readable format 
    return data




def get_source():
    api_url = 'https://newsapi.org/v1/sources'
    response = requests.get(api_url)
    data = response.json() # convert json to python-readable format
    return data




def examine_sources():
    data_sources= get_source()
    return data_sources






# def get_content_fromall():
