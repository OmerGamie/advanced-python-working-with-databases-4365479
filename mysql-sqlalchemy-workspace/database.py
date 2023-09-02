from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import registry

# Create an engine to connect to MySQL Database
# echo=True will turn on the logging of SQL queries, which can be useful for debugging
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/projects',
	echo=True)

# Create a registry to kepp track of classes 
mapper_registry = registry()
#mapper_registry.metadata

# Generate the base class for mapped classes from the registry
Base = mapper_registry.generate_base()

# Define a mapped class called 'Project'
class Project(Base):
  __tablename__ = 'projects'
  
  # Define columns for the table 'projects'
  Project_id = Column(Integer, primary_key=True)
  title = Column(String(50))
  description = Column(String(50))
  
  # Define the string representation of instances of the class
  def __repr__(self):
    return "<Project(title={0}, description={1})>".format(
      self.title, self.description)
