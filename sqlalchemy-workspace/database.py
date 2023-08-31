from sqlalchemy import create_engine, text

# Create a database in memory using SQLAlchemy
engine = create_engine('sqlite:///users-sqlite-alchemy.db', echo=True)

# Insert some users
users_to_insert = [{'first_name': 'John', 'last_name': 'Doey',
                    'email_address': 'john.doey@gmail.com'},
                   {'first_name': 'Omar', 'last_name': 'Little',
                    'email_address': 'omar.little@gmail.com'},
                   {'first_name': 'Bunk', 'last_name': 'Moreland',
                    'email_address': 'bunk_m@outlook.com'},
                   {'first_name': 'Percy', 'last_name': 'Whitmore',
                    'email_address': 'percy.whitmore@hotmail.com'}]

# Create a connection
conn = engine.connect()

# Create table
conn.execute(text('''CREATE TABLE IF NOT EXISTS Users
      (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
      first_name TEXT, last_name TEXT, email_address TEXT)'''))

# Insert data
conn.execute(text('''INSERT INTO Users (first_name, last_name, email_address)
      VALUES (:first_name, :last_name, :email_address)'''), users_to_insert)

# Query data
result = conn.execute(text('''SELECT * FROM Users'''))
for row in result:
    print(row)

# Commit the changes and close the connection
conn.commit()
conn.close()
