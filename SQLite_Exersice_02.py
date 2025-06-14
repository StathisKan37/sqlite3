# Excersice:
# ---------------------------------------------------------------------
# 1) Query the whiskies with less than 25 euros
# 2) Query everything except 7up
# 3) Query all the whiskies and the beers

import sqlite3

# Connecting to 'test_database.db' database
database_1 = sqlite3.connect('test_database.db')
# Creating a cursor
cursor = database_1.cursor()

# Optionally droping each table in 'test_database.db'
cursor.execute("DROP TABLE IF EXISTS table_1")

# Creating a table
cursor.execute("CREATE TABLE table_1(product text, category text, price numeric)")
# Inserting new values in table_1
products = [
	('Jameson', 'Whisky', 20.72),
	('Jameson Black', 'Whisky', 34.20),
	('Johnie Walker Red', 'Whisky', 16.90),
	('Grants', 'Whisky', 18.92),
	('Pepsi', 'Soft', 0.65),
	('Fanta lemon', 'Soft', 0.55),
	('Fanta orange', 'Soft', 0.55),
	('7up', 'Soft', 0.60),
	('Heineken', 'Beer', 1.55),
	('Corona', 'Beer', 1.44),
	('Bud', 'Beer', 1.53)
]
cursor.executemany("INSERT INTO table_1 VALUES (?,?,?)", products)

# Querying all the whiskies with less than 25 euros
print('WHISKIES CHEAPER THAN 25 EUROS:')
cursor.execute("SELECT * FROM table_1 WHERE category='Whisky' AND price<25")
for i in cursor.fetchall():
    print(f'{i[0]}  {i[1]}  {i[2]}')
print('-------------------------------')

# Querying everything except 7up
print('ALL DRINKS WITHOUT 7UP:')
cursor.execute("SELECT * FROM table_1 WHERE NOT product='7up'")
for i in cursor.fetchall():
    print(f'{i[0]}  {i[1]}  {i[2]}')
print('-------------------------------')

# Querying all whiskies and beers
print('ALL WHISKIES AND BEERS:')
cursor.execute("SELECT * FROM table_1 WHERE category='Whisky' OR category='Beer'")
for i in cursor.fetchall():
    print(f'{i[0]}  {i[1]}  {i[2]}')

# Commiting the table creation
database_1.commit()

# Closing the connection
database_1.close()
