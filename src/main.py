import database as db

import mysql.connector as c

# Driver code
if __name__ == "__main__":

    """
    Please enter the necessary information related to the DB at this place. 
    Please change PW and ROOT based on the configuration of your own system. 
    """
    PW = "Jaya@461998" # IMPORTANT! Put your MySQL Terminal password here.
    ROOT = "root"
    DB = "ecommerce_record" # This is the name of the database we will create in the next step - call it whatever you like.
    LOCALHOST = "localhost"
    connection = db.create_server_connection(LOCALHOST, ROOT, PW)

    # creating the schema in the DB
    # 1(b) Creating the tables using create_insert_method
    db.create_switch_database(connection, DB, DB)
    z = db.create_db_connection(LOCALHOST, ROOT, PW, DB)

    db.create_insert_query(z, query= "create table vendors (vendor_id varchar(10) primary key,  vendor_name varchar(45), vendor_email varchar(45), vendor_password varchar(45))")
    db.create_insert_query(z, query= "create table customers (customer_id varchar(10) primary key, customer_name varchar(45), customer_email varchar(45), customer_password varchar(45), address varchar(100))")
    db.create_insert_query(z, query= "create table orders (order_id int primary key, customer_id varchar(10) references customers(customer_id), vendor_id varchar(45) references vendors(vendor_id), total_value float, order_qunatity int , reward_point int)")
    db.create_insert_query(z, query= "create table items (product_id varchar(10) ,product_name varchar(20), product_price float, product_description varchar(100), vendor_id varchar(10) references vendors(vendor_id), emi_available varchar(10))")

    # Start implementing your task as mentioned in the problem statement
    # Implement all the test cases and test them by running this file
    #3(b) Find and print all the order details with total_value more than the average order value ordered from all customers





