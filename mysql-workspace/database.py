import mysql.connector as mysql
from mysql.connector import Error

# Create a connection to MySQL database
def connect(db_name):
  try:
    return mysql.connect(host='localhost', 
                         user='root', 
                         password='Doodijojo098/', 
                         database=db_name
                         )
  except Error as e:
    print(f"The error '{e}' occurred")


if __name__ == '__main__':
  db = connect("projects")
  cursor = db.cursor()
  cursor.execute("SELECT * FROM projects")
  project_records = cursor.fetchall()
  print(project_records)
  db.close()
  
  
