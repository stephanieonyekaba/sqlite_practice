import sqlite3


connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# this is how we order a record. DESC means descending
cursor.execute("""SELECT rowid, * FROM customers ORDER BY rowid DESC""")

items = cursor.fetchall()
for item in items:
    print(item)
connection.commit()


connection.close()
