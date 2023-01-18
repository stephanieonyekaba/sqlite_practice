import sqlite3


connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# this is how we update a record by its rowid (primary key)
cursor.execute(
    """UPDATE customers SET first_name = 'girly' WHERE rowid = 7  """)

# here we query the database
cursor.execute("""SELECT rowid, * FROM customers """)

items = cursor.fetchall()
for item in items:
    print(item)


# print("COMMAND EXECUTED CORRECTLY")

connection.commit()


connection.close()
