import sqlite3


connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# this is how we delete a record by its rowid (primary key)

cursor.execute("""DELETE from customers WHERE rowid = 2 """)

# querying our database
cursor.execute("""SELECT rowid, * FROM customers""")

items = cursor.fetchall()
for item in items:
    print(item)
connection.commit()


connection.close()
