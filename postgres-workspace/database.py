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
#cursor.execute('''CREATE TABLE SALES (ORDER_NUM INT PRIMARY KEY, 
#    CUST_NAME TEXT, 
#    PROD_NUMBER TEXT,
#    PROD_NAME TEXT,
#    QUANTITY INT,
#    PRICE REAL,
#    DISCOUNT REAL,
#    ORDER_TOTAL REAL);''')

sales = [ (1100935, "Spencer Educators", "DK204", "BYOD-300", 2, 89, 0, 178),
(1100948, "Ewan Ladd", "TV810", "Understanding Automation", 1, 44.95, 0, 44.95),
(1100963, "Stehr Group", "DS301", "DA-SA702 Drone", 3, 399, .1, 1077.3),
(1100971, "Hettinger and Sons", "DS306", "DA-SA702 Drone", 12, 250, .5, 1500),
(1100998, "Luz O'Donoghue", "TV809", "Understanding 3D Printing", 1, 42.99, 0, 42.99) ]

cursor.executemany("INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", sales)


# Commit the transaction
conn.commit()
conn.close()
