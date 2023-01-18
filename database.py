import sqlite3


connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# to insert many records at the same time we create a variable called many_customer
# in the dictionary many_customer, we can create several tupals (objects)
many_customer = [
    ('Pj', 'Watson', 'pw@gmail.com'),
    ('Tim', 'Jones', 'bb@gmail.com'),
    ('Sam', 'Anderson', 'hotgirl101@gmail.com'),
]

# we run the variable executemany and use the sql ? syntax
# we then pass in our variable many_customer
cursor.executemany(
    "INSERT INTO customers VALUES(?, ?, ?)", many_customer)


print("COMMAND EXECUTED CORRECTLY")

connection.commit()


connection.close()
