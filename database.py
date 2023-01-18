import sqlite3


connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# this is how we update a record
cursor.execute(
    """UPDATE customers SET first_name = 'Alex' WHERE last_name = 'Anderson'  """)

# here we query the database
cursor.execute("""SELECT * FROM customers """)

items = cursor.fetchall()
print(items)


# print("COMMAND EXECUTED CORRECTLY")

connection.commit()


connection.close()
