import sqlite3
sqlite_file = ".SSKT_curves.db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
conn.commit()
conn.close()
