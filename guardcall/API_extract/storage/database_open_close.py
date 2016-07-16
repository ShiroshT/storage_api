''' Connect to database '''

import os
import sqlite3
from TwitterSearch import *
from settings import *
import time

def close(conn):
    """ Commit changes and close connection to the database """
    conn.commit()
    conn.close()

def connect(sqlite_file):
    """ Make connection to an SQLite database file """
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return conn, c
