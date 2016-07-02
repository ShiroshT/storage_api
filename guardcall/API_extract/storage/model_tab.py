import os
import sqlite3

sqlite_file = '/Users/siyanetissera/development/scratch_space/API_test/guardcall/storage/APIStorage.sqlite'



def createDatabase():
    conn = sqlite3.connect(sqlite_file)
    print "Opened database successfully";

    conn.execute('''CREATE TABLE API_Store
           (ID INT PRIMARY KEY     NOT NULL,
           title           TEXT    NOT NULL,
           urllink          TEXT     NOT NULL,
           text             CHAR(50));''')
    print "Table created successfully";

    conn.close()



def comitetoDatabase(dataexport):


    sqlite_file = '/Users/siyanetissera/development/scratch_space/API_test/guardcall/API_extract/APIStorage.sqlite'

    # conn = sqlite3.connect(sqlite_file)
    # c = conn.cursor()
    # print "Opened database successfully";
    #
    # conn.execute('''CREATE TABLE API_Store
    #        (ID INT PRIMARY KEY     NOT NULL,
    #        title           TEXT    NOT NULL,
    #        urllink          TEXT     NOT NULL,
    #        text             CHAR(50));''')
    # print "Table created successfully";

    # conn.close()

    # exportData['response']['results'][1]['fields']['body']

    les = len(dataexport['response']['results'])

    conn = sqlite3.connect(sqlite_file)
    print "Opened database successfully";

    for i in xrange(les):

        valf = i
        titlea = dataexport['response']['results'][i]['fields']['headline']
        linka = dataexport['response']['results'][i]['fields']['headline']
        texta = dataexport['response']['results'][i]['fields']['body']

        conn.execute("insert into API_Store  values (?, ?,?,?)", (valf, titlea, linka, texta))

    conn.commit()
    conn.close()



