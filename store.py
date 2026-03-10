import sqlite3
from tabulate import tabulate

# Initialise the Database and insert intial values

con = sqlite3.connect("Store.db")
cur = con.cursor()

#cur.execute('CREATE TABLE items(id INTEGER PRIMARY KEY, name, price, quantity, category)')
#cur.execute('CREATE TABLE users(username, password, type)')
cur.execute('CREATE TABLE userinventory(username, items, quantity)')
#cur.execute(f"DROP TABLE IF EXISTS items") #delete entire table
#con.commit()

#cur.execute("""
#     INSERT INTO users VALUES
#         ('Chipsyyy', cool1234, admin)
#         ('customer', 1234, customer)
# """)
#con.commit()

# cur.execute(""" 
#     INSERT INTO items (name, price, quantity, category) VALUES
#         ('Apple', 2, 100, 'fruit'),
#         ('Banana', 1, 100, 'fruit'),
#         ('Pear', 3, 50, 'fruit'),
#         ('Steak', 20, 5, 'meat'),
#         ('Chicken Breast', 10, 20, 'meat'),
#         ('Pork Belly', 40, 2, 'meat')
#     """)

cur.execute("""
            INSERT INTO userinventory (username, items, quantity) VALUES
            (Chipsyyy, Apple, 5)
            """
)

# con.commit() #commit() method stores the entries into the disk 

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
            choice = int(input("""What would you like to do?
                                1. Buy an item
                                2. View invetory
                                3. Return to home page
                            """))
            
            if choice == 1: 
                self.buy()
            elif choice == 2:
                self.previewItems()
            else:
                main()
            pass
    
    def buy(self):
        df = pd.read_sql_query("SELECT * FROM items", con)
        
        print("\n--- Current Inventory ---")
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
        
        while True:
            itemID = input("What would you like to purchase? (Enter the ID number): ")
            buyQuantity = int(input("How much of that item would you like to buy? "))
            
            itemQuantityQuery = "SELECT quantity FROM items where id = ?"
            
            cur.execute(itemQuantityQuery, (itemID,))

            itemQuantity = cur.fetchone()

            if buyQuantity > itemQuantity[0]:
                print("You cannot purchase more stock than what is available!")
                continue
            else:     
                itemSearchQuery = """
                                UPDATE items
                                SET quantity = quantity - ?
                                WHERE id = ?
                                """
                
                cur.execute(itemSearchQuery, (buyQuantity, itemID))
                con.commit()
                cur.execute(f"SELECT name FROM items where id = {itemID}")
                itemName = "".join(cur.fetchone())
                if(itemName[-1] == "y" and buyQuantity > 1):
                    itemsWithY = itemName[:-1] + "ies"
                    print(f"You have bought {buyQuantity} {itemsWithY}")
                elif(itemName[-1] == "y" and buyQuantity == 1):
                    print(f"You have bought 1 {itemName}")
                else:
                    print(f"You have bought {buyQuantity} {itemName}s")
                return False
    
    def adminPage(self):
        choice = int(input("""What would you like to do?
                            1. Add an item
                            2. Restock an item
                            3. Remove an item
                            4. Return to home page
                            Choice: 
                        """))
        
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
        self.previewItems()
        itemID = input("What item do you want to restock? (Enter item ID): ")
        restockQuantity = int(input("What do you want to set the stock value to?: "))
        restockQuery = "SELECT quantity FROM items WHERE id = ?"

        cur.execute(restockQuery, (itemID,))
        cur.fetchone()

        updateQuery = ("""
                        UPDATE items
                       SET quantity = ?
                       WHERE id = ?                    
                    """)

        cur.execute(updateQuery, (restockQuantity, itemID))
        con.commit()
        cur.execute(f"SELECT name FROM items where id = {itemID}")
        itemName = "".join(cur.fetchone())
        print(f"You have set the stock value of {itemName} to {restockQuantity}")
        print("\n+------+----------------+---------+------------+------------+")
        self.customerDashboard()

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

    def previewItems(self):
        df = pd.read_sql_query("SELECT * FROM items", con)
        
        print("\n--- Current Inventory ---")
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

class User:
    def __init__(self, name):
        self.name = name

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

class Admin(User):
    pass

class Customer(User):
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
        