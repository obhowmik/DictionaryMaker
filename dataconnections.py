#SumanWorkTrack by Suman
import sys
import sqlite3
sys.dont_write_bytecode = True

#establishing data connection and cursor
global cn
global conn
conn = sqlite3.connect('DictionaryDB.db')  #connection to the database
cn = conn.cursor()  #creates the cursor
