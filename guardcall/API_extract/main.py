import os

from storage.model_tab import comitetoDatabase
from storage.model_tab import createDatabase
from apicall.guadcall import get_content

sqlite_file = '/Users/siyanetissera/development/scratch_space/API_test/guardcall/storage/APIStorage.sqlite'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


exportData = get_content()

# createDatabase()
comitetoDatabase(exportData)

# exportData['response']['results'][1]['fields']['body']