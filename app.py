import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

# Filtering by release year

release_year = (1985,)

cursor.execute('SELECT * FROM movies WHERE year=?', release_year)

print(cursor.fetchall())

connection.commit()
connection.close()
