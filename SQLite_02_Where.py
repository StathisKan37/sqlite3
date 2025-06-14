import sqlite3

# Connecting to 'test_database.db' database
database_1 = sqlite3.connect('test_database.db')
# Creating a cursor
cursor = database_1.cursor()

# Optionally droping each table in 'test_database.db'
cursor.execute("DROP TABLE IF EXISTS table_1")

# Creating a table
cursor.execute("CREATE TABLE table_1(first_name text,last_name text,email text)")
# Inserting new values in table_1
names_list = [
	('Name_1', 'Last_name_1', 'name1@mail.com'),
	('Name_2', 'Last_name_2', 'name2@mail.com'),
	('Name_3', 'Last_name_3', 'name3@mail.com'),
	('Name_4', 'Last_name_4', 'name4@mail.com')
]
cursor.executemany("INSERT INTO table_1 VALUES (?,?,?)", names_list)

# Query the row whith last name: 'Last_name_3'
cursor.execute("SELECT * FROM table_1 WHERE last_name = 'Last_name_3'")
for i in cursor.fetchall():
	print(f'{i[0]}  {i[1]}  {i[2]}')

# Commiting the table creation
database_1.commit()

# Closing the connection
database_1.close()
