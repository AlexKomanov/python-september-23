import sqlite3

# Create connection with DB
connection_manager = sqlite3.connect("gta.db")

# Create a cursor object (aka driver)
my_cursor = connection_manager.cursor()

my_cursor.execute("CREATE TABLE IF NOT EXISTS gta (release_date INTEGER, release_name TEXT, release_city TEXT)")

add_values_query_string = """
INSERT INTO gta VALUES (?,?,?)
"""

query_params = (2008, "Grand Theft Auto IV", "Liberty City")

my_cursor.execute(add_values_query_string, query_params)

connection_manager.commit()

# Close SQLite3 connection
my_cursor.close()
