from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, select
from sqlalchemy.orm import registry, relationship, Session

# Intialize the engine to connect to the database
engine = create_engine('mysql+mysqlconnector://root:new_password@localhost:3306/projects',
	echo=True)

# Create a registry to manage multiple mapped classes 
mapper_registry = registry()
#mapper_registry.metadata

# Create a base class for model definitions
Base = mapper_registry.generate_base()

# Define the Project class with its table and columns
class Project(Base):
	__tablename__ = 'projects'
	project_id = Column(Integer, primary_key=True)
	title = Column(String(length=50))
	description = Column(String(length=50))
  
  # String representation of the Project object
	def __repr__(self):
		return "<Project(title='{0}, description='{1}')>".format(
			self.title, self.description)

# Define the Task class with its table and columns
class Task(Base):
	__tablename__ = 'tasks'
	task_id = Column(Integer, primary_key=True)
	project_id = Column(Integer, ForeignKey('projects.project_id'))
	description = Column(String(length=50))
  
  # Establish a bidirectional relationship with the Project class
	project = relationship("Project")
  
  # String representation of the Task object
	def __repr__(self):
		return "<Task(description='{0}')>".format(self.description)

# Create all tables in the engine. This is equivalent to "Create Table"
Base.metadata.create_all(engine)

# Create a session to interact with the database
with Session(engine) as session:
  # Select the project with the title 'Organize closet'
  smt = select(Project).where(Project.title == 'Organize closet')
  results = session.execute(smt)
  organize_closet_project = results.scalars().first()
  
  # Fetch all tasks for the project
  smt = select(Task).where(Task.project_id == organize_closet_project.project_id)
  results = session.execute(smt)
  
  # Print each task for the project
  for task in results:
    print(task)











