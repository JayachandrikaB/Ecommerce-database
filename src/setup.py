import csv
import database as db

PW = "Jaya@461998" # IMPORTANT! Put your MySQL Terminal password here.
ROOT = "root"
DB = "ecommerce_record" # This is the name of the database we will create in the next step - call it whatever you like.
LOCALHOST = "localhost"


# # creating the schema in the DB
z = db.create_db_connection(LOCALHOST, ROOT, PW, DB)


RELATIVE_CONFIG_PATH = '../config/'
CUSTOMERS = 'customers'
VENDOR = 'vendors'
ITEM = 'items'
ORDER = 'orders'
#2(a) Insert method to perform insert operations in the tables
def insert(connection):
    cur = connection.cursor()
    return cur


# Create the tables through python code here
# if you have created the table in UI, then no need to define the table structure
# If you are using python to create the tables, call the relevant query to complete the creation

with open(RELATIVE_CONFIG_PATH+CUSTOMERS+'.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    val.pop(0)

    """
    Here we have accessed the file data and saved into the val data structure, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
# Inserting values into customer table
cur1 = insert(z)
insert_statement = """INSERT INTO customers(customer_id, customer_name , customer_email , customer_password, address) values(%s, %s, %s,%s, %s)"""
result = cur1.executemany(insert_statement, val)
z.commit()

with open(RELATIVE_CONFIG_PATH+VENDOR+'.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))

    val.pop(0)
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
# Inserting values into Vendors table
cur2 = insert(z)
insert_statement = """INSERT INTO vendors(vendor_id,vendor_name,vendor_email,vendor_password) values(%s, %s, %s,%s)"""
result = cur2.executemany(insert_statement, val)
z.commit()


with open(RELATIVE_CONFIG_PATH+ITEM+'.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))

    val.pop(0)
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
# Inserting values into Items table
cur3 = insert(z)
insert_statement = """INSERT INTO items(product_id, product_name, product_price, product_description, vendor_id , emi_available) values(%s, %s, %s,%s, %s, %s)"""
result = cur3.executemany(insert_statement, val)
z.commit()


with open(RELATIVE_CONFIG_PATH+ORDER+'.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))



    val.pop(0)
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
# Inserting values  from orders.csv into orders tables
cur4 = insert(z)
insert_statement = """INSERT INTO orders(order_id, customer_id, vendor_id, total_value, order_qunatity, reward_point) values(%s, %s, %s,%s, %s, %s)"""
result = cur4.executemany(insert_statement, val)
z.commit()
#2(b)
insert_statement = """INSERT INTO orders(order_id, customer_id, vendor_id, total_value, order_qunatity, reward_point) values(%s, %s, %s,%s, %s, %s)"""
records = [
        (101, 1, 1,34567, 1, 100),
        (102, 2, 2,35567, 2, 200),
        (103, 3, 3,36567, 1, 100),
        (104, 4, 4,37567, 3, 300),
        (105, 5, 5,38567, 4, 100),
    ]
cur5 = insert(z)
res = cur5.executemany(insert_statement, records)
z.commit()
#2(c) Fetching records from orders table
cur6 = insert(z)
cur6.execute("select * from orders")
for i in cur6:
    print(i)
z.commit()
''''
cur7 = insert(z)
cur7.execute("select * from orders group by customer_id having sum(total_value)")
#3

cur8 = insert(z)
z.cursor(buffered = True)
cur8.execute( "select * from orders a where total_value > (select avg(total_value) from orders b where b.customer_id = a.customer_id)")
cur8.fetchall()
for i in cur8:
    print(i)
z.commit() '''