import sqlite3

# Create a connection to the database
connection = sqlite3.connect('users-sqlite.db')

# Create a cursor object
cursor = connection.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
               first_name TEXT, last_name TEXT, email_address TEXT)''')

# Insert a multiple records using the executemany() method
users_to_insert = [ ('John', 'Doey', 'john.doey@gmail.com'),
                   ('Omar', 'Little', 'omar.little@gmail.com'),
                    ('Bunk', 'Moreland', 'bunk.moreland@hotmail.com'),
                    ('Percy', 'Whitmore', 'percy_c@outlook.com')]

cursor.executemany('''INSERT INTO users (first_name, last_name, email_address)
                  VALUES (?, ?, ?)''', users_to_insert)

# Select all records from the users table
cursor.execute('''SELECT * FROM users''')

# Print the results
print(cursor.fetchall())

# Commit the changes to the database
connection.commit()
connection.close()
