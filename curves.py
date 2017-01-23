import sqlite3
import json
import numpy as np

sqlite_file = ".SSKT_curves.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Curves
             (name text, currency text, vector text)''')

conn.commit()
conn.close()
