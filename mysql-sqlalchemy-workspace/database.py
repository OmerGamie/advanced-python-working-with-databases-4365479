import sqlalchemy

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:new_password@localhost:3306/projects', 
    echo=True)

