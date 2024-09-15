# sqlalchemy <- this library "database independent"
import sqlite3
db = sqlite3.connect('ragnews.db')
# no standard file extension for sqlite;
# you can see: .db, .sql, .sqlite, .sqlite3

cursor = db.cursor()
sql = '''
SELECT count(*) FROM articles;
'''
cursor.execute(sql)
row = cursor.fetchone()
print(f"row={row}")

cursor = db.cursor()
sql = '''
SELECT rowid, rank, title, publish_date, hostname, url, en_summary, text
FROM articles
WHERE articles MATCH 'Trump OR candidate OR nominee OR presidential OR election OR primary OR TBD OR voting OR politics OR Democrat OR candidacy'
ORDER BY rank DESC
LIMIT 10
'''
cursor.execute(sql)
rows = cursor.fetchall()
print('rows:', rows)
for row in rows:
    print(f"row={row}")
# make it ordered by how well the result matches the query
# take the top 10 of those
