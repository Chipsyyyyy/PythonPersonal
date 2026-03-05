import sqlite3
import pandas as pd

# Initialise the Database and insert intial values

con = sqlite3.connect("Store.db")
cur = con.cursor()

# cur.execute('CREATE TABLE items(id INTEGER PRIMARY KEY, name, price, stock, category)')
# cur.execute('CREATE TABLE users(username, password, type)')
#cur.execute(f"DROP TABLE IF EXISTS users") #delete entire table
con.commit()

#cur.execute("""
#     INSERT INTO users VALUES
#         ('Chipsyyy', cool1234, admin)
#         ('customer', 1234, customer)
# """)
#con.commit()

# cur.execute(""" 
#     INSERT INTO items (name, price, stock) VALUES
#         ('Apple', 2, 100, fruit),
#         ('Banana', 1, 100, fruit),
#         ('Pear', 3, 50, fruit),
#         ('Steak', 20, 5, meat),
#         ('Chicken Breast', 10, 20, meat),
#         ('Pork Belly', 40, 2, meat)
#     """)

con.commit() #commit() method stores the entries into the disk 

# all = cur.execute("SELECT name, price FROM store ORDER BY price")
# print(all.fetchall())

# cur.execute(f"DELETE FROM store WHERE id = 01") # Deleting rows
# cur.execute(f"DELETE FROM users WHERE username = 'Chipsyyy'")
#con.commit()

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
                regType = input("What type of user (Customer/Admin): ").lower()
                regQuery = "INSERT INTO users VALUES(?, ?, ?)"
                cur.execute(regQuery, (regUsername, regPassword, regType))
                con.commit()
                print("You've successfully registered!")
                main()
                return False
            else:
                print(f"The usernmame: {regUsername} already exists! Please try again")

    def login(self):
        
        while True:
                username = input("Enter your username: ")
                
                checkforUsername = "SELECT EXISTS(SELECT 1 FROM users WHERE username = ?)"
                    
                cur.execute(checkforUsername, (username,))

                exists = cur.fetchone()
                    
                if not bool(exists[0]):
                    print("That username does not exist! Please try again")
                    continue
            
                password = input("Enter your password: ")

                userquery = "SELECT EXISTS(SELECT 1 FROM users WHERE username = ? AND password = ?)"

                cur.execute(userquery, (username, password))

                userCheck = cur.fetchone()

                if not bool(userCheck[0]):
                    print("The username and password combination is wrong! Please try again")
                else:
                    
                    print(f"You are logged in as {username}")
                    # print(pd.read_sql_query("SELECT * FROM users", con)) #Print out in a pretty format
                    u1 = User()
                    u1.checkIfAdmin(username)
                    return False


    def deleteUser(self):
        delUsername = input("Which user do you want to delete? Enter their username: ")
        
        delUserQuery = "DELETE FROM users WHERE username = ?"
        
        print(f"User: {delUsername} has been deleted!")

        cur.execute(delUserQuery, (delUsername,))
        con.commit()
        
        pass

    def customerDashboard(self):
            choice = input("""What would you like to do?
                                1. Buy an item
                                2. View invetory
                                3. Return to home page
                            """)
            
            if choice == 1: 
                self.buy()
            elif choice == 2:
                self.viewInventory()
            else:
                main()
            pass
    
    def buy(self):
        pass

    def viewInventory():
        pass
    
    def adminPage(self):
        choice = input("""What would you like to do?
                            1. Add an item
                            2. Restock an item
                            3. Remove an item
                            4. Return to home page
                            Choice: 
                        """)
        
        if choice == 1: 
            self.addItem()
        elif choice == 2:
            self.restock()
        elif choice == 3:
            self.removeItem()
        else:
            main()
        pass    

    def restock(self):
        pass

    def addItem(self):
        itemCategory = input("Enter the item category (Fruit or Meat): ").lower()
        itemName = input("Enter the name of the item you want to add: ").lower()
        itemPrice = input("Enter the price of the item: ")
        itemStock = input("Enter the stock level for the item: ")

        addQuery = f"INSERT INTO items (name, price, stock, category) VALUES"
        
        cur.execute(addQuery, itemName, itemPrice, itemStock, itemCategory)
        con.commit()
        print(f"{itemName} has been successfully added!")

        pass

    def removeItem(self):
        itemName = input("Enter the name of the item you want to remove: ")
        removeQuery = "DELETE FROM items WHERE name = ?"
        cur.execute(removeQuery, itemName)
        con.commit()
        print(f"{itemName} has successfully been removed")
        #print(pd.read_sql_query("SELECT * FROM items", con))
        pass

    def previewItems():
        # all = cur.execute("SELECT * FROM items ORDER BY price")
        # print(all.fetchall())
        pass

class User:
    def createStore(self):
        self.store = Store()
        return self.store

    def checkIfAdmin(self, username):
        
        adminCheckQuery = "SELECT * FROM users WHERE username = ? AND type = ?"
        cur.execute(adminCheckQuery, (username, "admin"))
        isAdmin = cur.fetchone()

        if isAdmin:
            self.createStore().adminPage()
        else:
            self.createStore().customerDashboard()
        pass


    def customerDashboard(self):

        pass

def main():
    s1 = Store()
    choice = int(input("""What do you want to do?
                   1. Register
                   2. Log in
                   3. Delete User
                   4. Exit 
                   Choice: """))
    
    if choice == 1: 
            s1.register()
    elif choice == 2:
            s1.login()
    elif choice == 3:
            s1.deleteUser()
    else:
        exit("Thank you for using the store!")
    pass

if __name__ == "__main__":
    main()
        