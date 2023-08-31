import sqlalchemy

# Create a database using SQLAlchemy
engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True)

with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT * FROM movies"))
    for row in result:
        print(row)




