
import mysql.connector

# 1. Connect Python with MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pallavi@123"
)

print("Connection is successful")


# 2. Create cursor
cursor = conn.cursor()


# 3. Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS legend_player")

print("Database is created")


# 4. Select database
cursor.execute("USE legend_player")


# 5. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cricketers(
    name VARCHAR(50),
    age INT,
    runs INT
)
""")

print("Table has been created successfully")


# 6. Insert data
sql_query = """
INSERT INTO cricketers (name, age, runs)
VALUES (%s, %s, %s)
"""

data = [
    ("Rohit Sharma", 37, 21000),
    ("Virat Kohli", 36, 29000),
    ("AB", 38, 20000)
]

cursor.executemany(sql_query, data)

print("Values/data have been inserted")


# 7. Save the changes
conn.commit()


# 8. Display data
print("\n..... BEFORE UPDATING VALUES")

cursor.execute("SELECT * FROM cricketers")

for i in cursor:
    print(i)


# 9. UPDATE values
sql_query = """
UPDATE cricketers
SET runs = %s
WHERE name = %s
"""

data = (25000, "Rohit Sharma")

cursor.execute(sql_query, data)

conn.commit()


# 10. Display updated data
print("\n..... AFTER UPDATING VALUES")

cursor.execute("SELECT * FROM cricketers")

for i in cursor:
    print(i)


# 11. Close connection
conn.close()

print("\nConnection closed")

# 12. DELETE DATA
sql_query = """
DELETE FROM cricketers
WHERE name = %s
"""

data = ("Virat Kohli",)

cursor.execute(sql_query, data)

conn.commit()

print("Virat Kohli record deleted")


# 10. Display updated data
print("\n..... AFTER DELETING VALUES")

cursor.execute("SELECT * FROM cricketers")

for i in cursor:
    print(i)


# 11. Close connection
conn.close()

print("\nConnection closed")


# import mysql.connector
# conn=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Pallavi@123")
# print("connection is successfull for the database")

# cursor=conn.cursor()

# cursor.execute("Create Database if not EXISTS legend_player")

# print("Database is created")
# cursor.execute(" USE Legend players")

# cursor.execute("""create table criketers(name varchar(20), age int, runs int)""")

# print(" Table has been create succesfully ")

# sql_query= " INSERT INTO Cricket (name, age, runs) values(%$,%$,%$)"

# data=[("Rohit Sharma",37, 21000),
#       ("Virat Kohli",36, 29000),
#       ("Ab",38, 20000)]

# cursor.executemany(sql_query,data)

# print("Values/data has been insert")

# conn.commit()         # xcursor.commit

# cursor.execute(" SELECT * From Cricketers ")

# for i in cursor:
#     print(i)
# conn.close()

# # UPDATING VALUES

# print("\n ..... BEFORE UPDATING VALUES")

# sql_query="""UPDATE cricketers
# SET runs=%$
# where name="Rohit Sharma" 
# """

# data=[25000]

# conn.commit()
# cursor.execute(" SELECT * from Cricketers")
