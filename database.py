import sqlite3

# in order for us to do anything we need to create a connection to a database we will create.
# we pass in the name of the database in the parentheses

connection = sqlite3.connect('customer.db')

# we create a cursor so we can make a table
# we establish a connection
cursor = connection.cursor()

# here we are defining the paramaters of our table. we want the datatype of each to be text
cursor.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
)""")

# here we are commiting so the table 'customers' is pushed into our database 'connection'
connection.commit()

# this command just closes our connection after we commit it
connection.close()
