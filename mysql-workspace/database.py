import mysql.connector as mysql

# Function to connect to the database
def connect(db_name):
	try:
		return mysql.connect(host="localhost",
							 database=db_name,
							 user='root',
							 password="new_password")
	except Error as e:
   # print any errors that occurs
		print(e)
  
# Function to add a new project to the database
def add_project(cursor, project_title, project_description, tasks):
  # Data to fill new projects
  project_data = (project_title, project_description)
  
  # Insert the new project to the projects table
  cursor.execute("""INSERT INTO projects (title, description) 
        VALUES (%s, %s)""", project_data)
  
  # Prepare data for the tasks associated with the new project
  tasks_data = []
  for task in tasks:
    task_data = (cursor.lastrowid, task)
    tasks_data.append(task_data)
    
  # Insert the tasks into the tasks table  
  cursor.executemany("""INSERT INTO tasks (project_id, description)
				VALUES (%s, %s)""", tasks_data)
 
# Entry point of the script  
if __name__ == '__main__':
  # Connect to the 'projects' database
	db = connect("projects")

  # Create a cursor object
	cursor = db.cursor()

  # Task descriptions for the project
	tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
 
  # Add a new project and its tasks to the database
	add_project(cursor, "Clean house", "Clean house by room", tasks)
 
  # Commit the changes to the database 
	db.commit()

  # Query and print all records from the 'projects' table
	cursor.execute("SELECT * FROM projects")
	project_records = cursor.fetchall()
	print(project_records)
  
  # Query and print all records from the 'tasks' table
	cursor.execute("SELECT * FROM tasks")
	tasks_records = cursor.fetchall()
	print(tasks_records)