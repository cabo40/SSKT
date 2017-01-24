import sqlite3
import json

sqlite_file = ".SSKT_curves.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Curves
             (name text, currency text, vector text)''')

conn.commit()
conn.close()
###For the moment it doesn't seem like a curve object or curve properties... but it will... :)
