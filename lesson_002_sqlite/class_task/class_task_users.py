import sqlite3

# Parameters to fill
title = input("Enter your title (Mr. Ms.): ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

# Define connection manager
connect_manager = sqlite3.connect("users.db")

# Define cursor
cursor = connect_manager.cursor()

# Query to execute
table_create_query = """
CREATE TABLE IF NOT EXISTS users (title TEXT, first_name TEXT, 
last_name TEXT, age INT, address TEXT)
"""

# Create SQL table
connect_manager.execute(table_create_query)


# Query of insert data to execute
data_insert_query = """
INSERT INTO users (title, first_name, 
last_name, age, address) VALUES (?,?,?,?,?)
"""

# Data structure
data_insert_tuple = (title, first_name, last_name, age, address)

cursor.execute(data_insert_query, data_insert_tuple)

connect_manager.commit()

print(cursor.execute("SELECT * FROM users"))
for row in cursor.execute("SELECT * FROM users"):
    print(row)

connect_manager.close()
