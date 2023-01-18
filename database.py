import sqlite3


connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# here we are running a query to show everything in our customers database
cursor.execute("SELECT * FROM customers")

items = cursor.fetchall()

for item in items:
    print(item)


# print("COMMAND EXECUTED CORRECTLY")

connection.commit()


connection.close()
