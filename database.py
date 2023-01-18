import sqlite3


connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# this is how we query our database using AND/OR clause
cursor.execute(
    """SELECT rowid, * FROM customers WHERE last_name = 'Onyekaba' OR rowid = 3 """)

items = cursor.fetchall()
for item in items:
    print(item)
connection.commit()


connection.close()
