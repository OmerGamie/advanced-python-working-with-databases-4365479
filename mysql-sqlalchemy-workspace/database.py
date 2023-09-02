from sqlalchemy import Column, String, Integer, Numeric, create_engine, desc
from sqlalchemy.orm import registry, Session

# Intialize SQLAlchemy engine
engine = create_engine(
    'mysql+mysqlconnector://root:new_password@localhost:3306/red30',
    echo=True)

# Intialize ORM mapper registry
mapper_registry = registry()

# Base class for ORM models
Base = mapper_registry.generate_base()

# Sale class mapped to sales table
class Sale(Base):
	__tablename__ = 'sales'

	order_num = Column(Integer, primary_key=True)
	cust_name = Column(String)
	prod_number = Column(String)
	prod_name = Column(String)
	quantity = Column(Integer)
	price = Column(Numeric)
	discount = Column(Numeric)
	order_total = Column(Numeric)
  
  # String representation of Sale object
	def __repr__(self):
		return "<Sale(order_num='{0}', cust_name='{1}', prod_name='{2}', quantity='{3}', order_total='{4}')>".format(self.order_num, self.cust_name, self.prod_name, self.quantity, self.order_total)

# Create tables in database
Base.metadata.create_all(engine)

# Create session for database operations
with Session(engine, future=True) as session:
  sales_data = [
        Sale(order_num=1, cust_name='John Doe', prod_number='P1', prod_name='Laptop', quantity=1, price=1000, discount=0, order_total=1000),
        Sale(order_num=2, cust_name='Jane Doe', prod_number='P2', prod_name='Phone', quantity=2, price=500, discount=0, order_total=1000),
        Sale(order_num=3, cust_name='Sam Smith', prod_number='P3', prod_name='TV', quantity=1, price=1500, discount=0, order_total=1500),
        Sale(order_num=4, cust_name='Emily Brown', prod_number='P4', prod_name='Camera', quantity=2, price=700, discount=0, order_total=1400),
        Sale(order_num=5, cust_name='Chris Evans', prod_number='P5', prod_name='Headphone', quantity=3, price=300, discount=0, order_total=900)
    ]
  
   # Flush the session to obtain the primary key values
  session.flush()
  
  # Bulk insert sales data into the database
  session.bulk_save_objects(sales_data)
  session.commit()
  
  # Query the database to get the most expensive order
  most_expensive_order = session.query(Sale).order_by(desc(Sale.order_total)).first()
  print(f"Most expensive order: {most_expensive_order}")
  
  # Discover who ordered the most expensive order
  print(f"Customer who ordered the most expensive order: {most_expensive_order.cust_name}")
  

