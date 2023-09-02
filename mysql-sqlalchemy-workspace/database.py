from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import registry, relationship, Session

# Initialize the database engine connection
engine = create_engine('mysql+mysqlconnector://root:new_password@localhost:3306/projects',
	echo=True)

# Create a registry to manage mapped classes
mapper_registry = registry()
#mapper_registry.metadata

# Generate a base class for declarative class definitions
Base = mapper_registry.generate_base()

# Defone the Project class and its table and columns
class Project(Base):
	__tablename__ = 'projects'
	project_id = Column(Integer, primary_key=True)
	title = Column(String(length=50))
	description = Column(String(length=50))
  
  # String representation of the object for debugging
	def __repr__(self):
		return "<Project(title='{0}, description='{1}')>".format(
			self.title, self.description)

# Define the Task class and its table and columns
class Task(Base):
	__tablename__ = 'tasks'
	task_id = Column(Integer, primary_key=True)
	project_id = Column(Integer, ForeignKey('projects.project_id'))
	description = Column(String(length=50))
  
  # Establish a relationship between the Task and Project classes
	project = relationship("Project")
  
  # String representation of the object for easier debugging
	def __repr__(self):
		return "<Task(description='{0}')>".format(self.description)

# Create all tables
Base.metadata.create_all(engine)

# Creat a session to interact with the database
with Session(engine) as session:
  # Create a new project
  organize_closet_project = Project(title='Organize closet', 
          description='Organize the closet by color and style')
  
  # Add the project to the session
  session.add(organize_closet_project)
  
  # Flush the session to obtain the project id
  session.flush()
  
  # Define a list of tasks to add to the project
  tasks = [
    Task(project_id=organize_closet_project.project_id,
         description='Decide which clothes to donate'),
    Task(project_id=organize_closet_project.project_id,
         description='Organize summer clothes'),
    Task(project_id=organize_closet_project.project_id,
         description='Organize winter clothes')
	]
  
  # Bulk save the tasks into session
  session.bulk_save_objects(tasks)
  
  # Commit the changes
  session.commit()
  










