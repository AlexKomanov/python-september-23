import sqlite3

# Create connection with DB
connection_manager = sqlite3.connect("gta.db")

# Create a cursor object (aka driver)
my_cursor = connection_manager.cursor()

my_cursor.execute("CREATE TABLE IF NOT EXISTS gta (release_date INTEGER, release_name TEXT, release_city TEXT)")

add_values_query_string = """
INSERT INTO gta VALUES (?,?,?)
"""

# query_params = (2008, "Grand Theft Auto IV", "Liberty City")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

# for query in release_list:
#     my_cursor.execute(add_values_query_string, query)

# my_cursor.execute(add_values_query_string, query_params)

# my_cursor.executemany(add_values_query_string, release_list)

connection_manager.commit()

all_data = my_cursor.execute('SELECT * FROM  gta')

for row in all_data:
    print(row)


# Close SQLite3 connection
my_cursor.close()
