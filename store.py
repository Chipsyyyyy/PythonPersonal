import sqlite3

# Initialise the Database and insert intial values

con = sqlite3.connect("Store.db")
cur = con.cursor()

#cur.execute('CREATE TABLE store(id, name, price)')
#cur.execute('CREATE TABLE users(username, password)')

#cur.execute("""
#     INSERT INTO users VALUES
#         ('Chipsyyy', 1234)
# """)
#con.commit()

# cur.execute(""" 
#     INSERT INTO store VALUES
#         (01, 'Reaver Vandal', 500.00),
#         (02, 'Toy Axe', 25.00),
#         (03, 'Golden Pear', 39.99)
#     """)
# con.commit() #commit() method stores the entries into the disk 

# all = cur.execute("SELECT name, price FROM store ORDER BY price")
# print(all.fetchall())

# cur.execute(f"DELETE FROM store WHERE id = 01") # Deleting rows
# cur.execute(f"DELETE FROM users WHERE username = 'Chipsyyy'")
# con.commit()

# -------------------------------------------------------------------------------------------------------------------

class Store:

    def register(self):
        while True:
            regUsername = input("Enter a username: ")
            # Check if that username already exists in the database
            usernameQuery = "SELECT EXISTS(SELECT 1 FROM users WHERE username = ?)"
            
            cur.execute(usernameQuery, (regUsername,))

            usernameCheck = cur.fetchone()

            if not bool(usernameCheck[0]):
                regPassword = input("Enter a password: ")
                regQuery = "INSERT INTO users VALUES(?, ?)"
                cur.execute(regQuery, (regUsername, regPassword))
                con.commit()
                print("You've successfully registered!")
                return False
            else:
                print(f"The usernmame: {regUsername} already exists! Please try again")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password")

        userquery = "SELECT EXISTS(SELECT 1 FROM users WHERE username = ? AND password = ?)"

        cur.execute(userquery, (username, password))

        userCheck = cur.fetchone()

        if not bool(userCheck[0]):
            print("The username and password combination is wrong! Please try again")
        else:
            print(f"You are logged in as {username}")

    def deleteUser(self):
        delUsername = input("Which user do you want to delete? Enter their username: ")
        
        delUserQuery = "DELETE FROM users WHERE username = ?"
        
        print(f"User: {delUsername} has been deleted!")

        cur.execute(delUserQuery, (delUsername,))
        con.commit()
        
        pass


    def buy(self):
        pass

    def restock(self):
        pass

    def addItem(self):
        pass

    def removeItem(self):
        pass

class User:
    def __init__(self):
        username = self.username
        password = self.password
        pass

def main():
    s1 = Store()
    choice = int(input("""What do you want to do?
                   1. Register
                   2. Log in
                   3. Delete User
                   Choice: """))
    
    if choice == 1: 
            s1.register()
    elif choice == 2:
            s1.login()
    elif choice == 3:
            s1.deleteUser() 
    
    # username = input("Please enter your )username: ")
    # password = input("Please enter your password: ")
    # s1.login(username, password)
    #s1.register()
    #s1.deleteUser()

if __name__ == "__main__":
    main()
        