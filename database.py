import sqlite3


connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# here we are running a query to show everything in our customers database
cursor.execute("SELECT * FROM customers")

# we can then run several different commands
# connection.fetcone() --> this will display the last record added to our database
# connection.fetchmany(2) --> this will fetch two records in our database
# connection.fetchall() --> this will fetch all the records in our database

# we wrap our command in a print statement so we can see it in the terminal

# this will feth the first record in our table and return the item in the 2nd index
# of that record(email address)

print(cursor.fetchone()[2])

# print("COMMAND EXECUTED CORRECTLY")

connection.commit()


connection.close()
