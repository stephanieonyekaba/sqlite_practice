import sqlite3


connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# we can use the 'WHERE' clause to select certain paramaters for our records
cursor.execute("SELECT * FROM customers WHERE last_name = 'Onyekaba' ")

items = cursor.fetchall()

for item in items:
    print(item[0])


# print("COMMAND EXECUTED CORRECTLY")

connection.commit()


connection.close()
