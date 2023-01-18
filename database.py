import sqlite3

# in order for us to do anything we need to create a connection to a database we will create.
# we pass in the name of the database in the parentheses

connection = sqlite3.connect('customer.db')

# we create a cursor so we can make a table
# we establish a connection
cursor = connection.cursor()

# we are just running sql commands now to insert a record into our customers database. remember that
# sql commands are always capitalized
cursor.execute(
    "INSERT INTO customers VALUES('Mich', 'Onyekaba', 'm.o@gmail.com')")

# here i just wrote a print statement to show that teh command was
# executed correctly each time we run python3 database.py (remember database.py is the file name)
print("COMMAND EXECUTED CORRECTLY")

# here we are commiting so the table 'customers' is pushed into our database 'connection'
connection.commit()

# this command just closes our connection after we commit it
connection.close()
