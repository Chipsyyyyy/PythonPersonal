import sqlite3

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
#cur.execute(f"DELETE FROM users WHERE username = 'Chipsyyy'")

# -------------------------------------------------------------------------------------------------------------------

class Store:
    def login(username):
        usernamequery = "SELECT EXISTS(SELECT 1 FROM users WHERE username = ?)"
    
        cur.execute(usernamequery, (username,))
    
        usernameCheck = cur.fetchone()
    
        if not bool(usernameCheck[0]):
            print("The username and password combination is wrong! Please try again")
        else:
            pass #add password feature 


    def buy():
        pass

    def restock():
        pass

    def addItem():
        pass

    def removeItem():
        pass

class User:
    def __init__(self):
        username = self.username
        password = self.password
        pass

def main():
    s1 = Store
    username = input("Please enter your username: ")
    s1.login(username)
    pass

if __name__ == "__main__":
    main()
        