import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

famous_films = [('The Dark Knight', 'Christopher Nolan', 2008), 
('The Godfather', 'Francis Ford Coppola', 1972), 
('Pulp Fiction', 'Quentin Tarantino', 1994), 
('The Lord of the Rings: The Return of the King', 'Peter Jackson', 2003), 
('The Good, the Bad and the Ugly', 'Sergio Leone', 1966), 
('Moonrise Kingdom', 'Wes Anderson', 2012), 
('The Expandables', 'Sylvester Stallone', 2010), 
('The Hangover', 'Todd Phillips', 2009), 
('The Matrix', 'Lana Wachowski', 1999)]

cursor.executemany('''INSERT INTO movies(title, director, year) VALUES(?,?,?)''', famous_films)

cursor.execute('''SELECT * FROM movies''')

print(cursor.fetchall())

connection.commit()
connection.close()
