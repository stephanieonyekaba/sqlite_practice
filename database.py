import sqlite3


connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# this is how we query our database to limit the number of records we get
cursor.execute(
    """SELECT rowid, * FROM customers WHERE last_name = 'Onyekaba' ORDER BY rowid DESC LIMIT 2 """)

items = cursor.fetchall()
for item in items:
    print(item)
connection.commit()


connection.close()
