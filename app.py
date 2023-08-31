import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

funny_films = [('The Big Lebowski', 'Coen Brothers', '1998'),
('Rush Hour', 'Brett Ratner', '1998'),
('The Hangover', 'Todd Phillips', '2009'),
('Ted', 'Seth MacFarlane', '2012')]

cursor.executemany('''INSERT INTO movies(title, director, year)
 VALUES(?,?,?)''', funny_films)

cursor.execute('''SELECT * FROM movies''')



print(cursor.fetchall())

connection.commit()
connection.close()