import sqlite3

# Connecting to 'test_database.db' database
database_1 = sqlite3.connect('test_database.db')

# Creating a cursor
cursor = database_1.cursor()

# Optionally droping each table in 'test_database.db'
cursor.execute("DROP TABLE IF EXISTS table_1")

# Creating a table
cursor.execute("""
	CREATE TABLE table_1(
	first_name text,
	last_name text,
	email text
	)
""")
# Datatypes:
# 1) NULL
# 2) INTEGER
# 3) REAL
# 4) TEXT
# 5) BLOB

# Inserting a new value in table_1
cursor.execute("INSERT INTO table_1 VALUES ('Name_1', 'Last_name_1', 'name1@mail.com')")

# Inserting many values in table_1
names_list = [
	('Name_2', 'Last_name_2', 'name2@mail.com'),
	('Name_3', 'Last_name_3', 'name3@mail.com'),
	('Name_4', 'Last_name_4', 'name4@mail.com')
]
cursor.executemany("INSERT INTO table_1 VALUES (?,?,?)", names_list)

# Query the primary key and the database
cursor.execute("SELECT rowid, * FROM table_1")
for i in cursor.fetchall():
	print(f'{i[0]}  {i[1]}  {i[2]}  {i[3]}')

# Commiting the table creation
database_1.commit()

# Closing the connection
database_1.close()
