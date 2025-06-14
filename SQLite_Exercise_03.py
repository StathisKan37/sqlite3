# Excersice:
# ---------------------------------------------------------------------
# 1. Query the Honda and Toyota cars
# 2. Query the cars with models ending in 'a' or 5
# 3. Query the cars that contain 't' followed by 'a' in models

import sqlite3

# Connecting to 'test_database.db' database
database_1 = sqlite3.connect('test_database.db')
# Creating a cursor
cursor = database_1.cursor()

# Optionally droping each table in 'test_database.db'
cursor.execute("DROP TABLE IF EXISTS table_1")

# Creating a table
cursor.execute("CREATE TABLE table_1(brand text, model text, year integer)")
# Inserting new values in table_1
cursor.execute("""
INSERT INTO table_1 (brand, model, year) VALUES
	('Honda', 'Civic', 2020),
	('Honda', 'Accord', 2019),
	('Toyota', 'Corolla', 2021),
	('Toyota', 'Camry', 2020),
	('Ford', 'Mustang', 2018),
	('Ford', 'F-150', 2021),
	('Audi', 'A4', 2020),
	('Audi', 'Q5', 2022),
	('BMW', '3 Series', 2021),
	('BMW', 'X5', 2020),
	('Mazda', 'CX-5', 2022),
	('Nissan', 'Altima', 2019),
	('Nissan', 'Sentra', 2021);
""")

# 1. Querying all Honda and Toyota cars
print("ALL HONDA AND TOYOTA CARS:")
cursor.execute("SELECT * FROM table_1 WHERE brand IN ('Honda', 'Toyota')")
for i in cursor.fetchall():
    print(f'{i[0]}  {i[1]}  {i[2]}')
print('-------------------------------')

# 2. Querying all the cars with models ending in 'a' or 5
print("ALL CARS ENDING IN 'A' OR 5:")
cursor.execute("SELECT * FROM table_1 WHERE model LIKE '%a' OR model LIKE '%5'")
for i in cursor.fetchall():
    print(f'{i[0]}  {i[1]}  {i[2]}')
print('-------------------------------')

# 3. Querying all the cars that contain 't' followed by 'a' in models
print("MODELS CONTAINING 'T' FOLLOWED BY 'A':")
cursor.execute("SELECT * FROM table_1 WHERE model LIKE '%t%a%'")
for i in cursor.fetchall():
    print(f'{i[0]}  {i[1]}  {i[2]}')

# Commiting the table creation
database_1.commit()

# Closing the connection
database_1.close()
