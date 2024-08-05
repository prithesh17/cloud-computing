import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="database-1.cls8uu6iyupn.ap-northeast-1.rds.amazonaws.com",  # public-endpoint
    user="admin",
    password="u64FelfCSiauTdge3UfU"
)

# Create a cursor object
cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS my_new_database")
conn.commit()

# Confirm the database creation
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

# Create a new table
create_table_query = """
CREATE TABLE IF NOT EXISTS my_new_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(100)
)
"""

cursor.execute("USE my_new_database")
cursor.execute(create_table_query)

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

# Insert data into the table
insert_query = """
INSERT INTO my_new_table (name, age, email)
VALUES (%s, %s, %s)
"""
data = ("John Doe", 30, "john.doe@example.com")

# Execute the insert query
cursor.execute(insert_query, data)
conn.commit()  # Ensure the insert is committed

# Fetch and print all rows from the table
cursor.execute("SELECT * FROM my_new_table")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
