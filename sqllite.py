import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("student.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE IF NOT EXISTS student (
    name TEXT,
    class TEXT,
    section TEXT
);
"""

cursor.execute(table_info)

# Insert records (note: use quotes for string values)
cursor.execute("INSERT INTO student VALUES ('pruthvi', '10', 'A')")
cursor.execute("INSERT INTO student VALUES ('rachi', '11', 'B')")
cursor.execute("INSERT INTO student VALUES ('pooja', '12', 'C')")
cursor.execute("INSERT INTO student VALUES ('sham', '9', 'D')")

# Commit changes to save them in the database
connection.commit()

# Fetch and display the data
print("The inserted records are:")
data = cursor.execute("SELECT * FROM student")
for row in data:
    print(row)

connection.close()
