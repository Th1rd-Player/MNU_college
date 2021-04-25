import sqlite3
conn = sqlite3.connect(r'stud.db')
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS 'student'(
   user_id TEXT,
   course TEXT,
   group_us TEXT,
   status TEXT,
   username TEXT);
""")
conn.commit()