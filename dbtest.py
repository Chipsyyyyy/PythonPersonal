import sqlite3

with sqlite3.connect("my_database.db") as connection: # Establish the connection to the database file (the file name for the database is whatever is within the braces)
    cursor = connection.cursor() # Create an object to interact with the database

    cursor.execute( # Executes SQL statements
        ''' 
        CREATE TABLE IF NOT EXISTS users ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER )
    '''
    )

    cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", ("Alice", 20))
    cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", ("Maxwell", 21))

    cursor.execute("SELECT name, age FROM users")
    users = cursor.fetchall() # fetch methods retrieve rows from the database
    
    print("Users in the database:")
    for user in users:
        print(f"Name: {user[0]}, Age: {user[1]}")