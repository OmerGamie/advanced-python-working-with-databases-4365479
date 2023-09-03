import psycopg2

# Initialize a connection to the PostgreSQL database
conn = psycopg2.connect(database="red30",
    user="postgres",
    password="password",
    host="localhost",
    port="5432")

# Create a cursor object
cursor = conn.cursor()

# Create a table called SALES using the cursor object
cursor.execute('''CREATE TABLE SALES (ORDER_NUM INT PRIMARY KEY, 
    CUST_NAME TEXT, 
    PROD_NUMBER TEXT,
    PROD_NAME TEXT,
    QUANTITY INT,
    PRICE REAL,
    DISCOUNT REAL,
    ORDER_TOTAL REAL);''')

# Commit the transaction
conn.commit()
conn.close()
