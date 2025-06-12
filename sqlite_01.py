
# inserting new values in customers
cursor.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")

# inserting many values in customers
many_customers=[
  ('name_1', 'last_name_1', 'name1@mail.com'),
  ('name_2', 'last_name_2', 'name2@mail.com'),
  ('name_3', 'last_name_3', 'name3@mail.com'),
]
cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Query the database
cursor.execute("SELECT * FROM customers")
print(cursor.fetchall())
