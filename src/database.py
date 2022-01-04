import mysql.connector
import mysql.connector.cursor

# Global methods to push interact with the Database

# This method establishes the connection with the MySQL

def create_server_connection(host_name, user_name, user_password):

    x = mysql.connector.connect(host = host_name, user = user_name, passwd= user_password)
    return x
    pass
    # This is the name of the database we will create in the next step - call it whatever you like.

    # Implement the logic to create the server connection


# This method will create the database
def create_switch_database(connection, db_name, switch_db):
    cur = connection.cursor()
    cur.execute("create database ecommerce_record ")
    connection.commit()

# For database creation use this method
# If you have created your database using UI, no need to implement anything
 #pass

# This method will establish the connection with the newly created DB
#1(a) creating the schema and establishing connection with new db.
def create_db_connection(host_name, user_name, user_password, db_name):
    y = mysql.connector.connect(host=host_name, user=user_name, passwd=user_password, db = db_name)
    return y


   # pass
# Perform all single insert statments in the specific table through a single function call
# Logic to create table
def create_insert_query(connection, query):
# This method will perform creation of the table
# this can also be used to perform single data point insertion in the desired table
    cur = connection.cursor()
    cur.execute(query)
    cur.fetchall()
    connection.commit()

    pass
 #retrieving the data from the table based on the given query
def select_query(connection, query):
    # fetching the data points from the table
    cur = connection.cursor()
    cur.execute(query)
    cur.fetchall()
    #for i in cur:
    print(cur)


    # pass

# performing the execute many query over the table, 
# this method will help us to insert multiple records using a single instance
'''def insert_many_data(connection, sql, val):
    # to perform multiple insert operation in the database
    pass '''
