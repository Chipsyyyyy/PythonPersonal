from flask import Flask, render_template, request, redirect, url_for
from tabulate import tabulate
import sqlite3

def get_db_connection():
    con = sqlite3.connect('maxstore.db')
    con.row_factory = sqlite3.Row
    return con

app = Flask(__name__)

# cur.execute('CREATE TABLE items(id INTEGER PRIMARY KEY, name, price, quantity, category)')
# cur.execute('CREATE TABLE users(username, password, type)')

class Store:

    def register(self, regUsername, regPassword, regType):
        with get_db_connection() as con:
            cur = con.cursor()
        # Check if that username already exists in the database
            usernameQuery = "SELECT EXISTS(SELECT 1 FROM users WHERE username = ?)"
        
            cur.execute(usernameQuery, (regUsername,))

            usernameCheck = cur.fetchone()

            if not bool(usernameCheck[0]):
                regQuery = "INSERT INTO users VALUES(?, ?, ?)"
                cur.execute(regQuery, (regUsername, regPassword, regType))
                con.commit()
                return True
            else:
                print(f"The usernmame: {regUsername} already exists! Please try again")
                con.close()
                return False
        
    def login(self, username):
        with get_db_connection() as con:
            cur = con.cursor()

            while True:                    
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
                        return False
                    u1 = User()
                    u1.checkIfAdmin(username)                   
                    
    def deleteUser(self):
        with get_db_connection() as con:
            cur = con.cursor()
            delUsername = input("Which user do you want to delete? Enter their username: ")
            
            delUserQuery = "DELETE FROM users WHERE username = ?"
            
            print(f"User: {delUsername} has been deleted!")

            cur.execute(delUserQuery, (delUsername,))
            con.commit()
            

    def customerDashboard(self):
            
            pass
    
    def buy(self):
        with get_db_connection() as con:
            cur = con.cursor()
            self.previewItems()
            
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
        
        pass    

    def restock(self):
        with get_db_connection() as con:
            cur = con.cursor()
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
        with get_db_connection() as con:
            cur = con.cursor()
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
        with get_db_connection() as con:
            cur = con.cursor()
            itemName = input("Enter the name of the item you want to remove: ")
            removeQuery = "DELETE FROM items WHERE name = ?"
            cur.execute(removeQuery, itemName)
            con.commit()
            print(f"{itemName} has successfully been removed")

    def previewItems(self):
        with get_db_connection() as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM items")
            query = cur.fetchall()
        
        print("\n--- Current Inventory ---")
        print(tabulate(query, headers='keys', tablefmt='psql', showindex=False))
                    
class User:

    def createStore(self):
        self.store = Store()
        return self.store

    def checkIfAdmin(self, username):
        with get_db_connection() as con:
            cur = con.cursor()
            adminCheckQuery = "SELECT * FROM users WHERE username = ? AND type = ?"
            cur.execute(adminCheckQuery, (username, "admin"))
            isAdmin = cur.fetchone()

            if isAdmin:
                return True
            else:
                return False

s1 = Store()
u1 = User()

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_type = request.form.get('type')
        success = s1.register(username, password, user_type)
        
        if success:
            return redirect(url_for('home_page'))
        else:
            return "Username already exists! <a href='/register'>Try again</a>"
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        success = s1.login(username, password)

        if success == True:
            return redirect(url_for('admin_page'))
        elif success == False:
            return redirect(url_for('customer_page'))
        else:
            return "Username and Password combination is not correct! <a href='/login'> Try Again</a>"
    return render_template('login.html')

@app.route('/adminpage', methods=['GET', 'POST'])
def admin_page():
    return render_template('adminpage.html')


@app.route('/customerpage', methods=['GET', 'POST'])
def customer_page():
    return render_template('customerpage.html')


if __name__ == '__main__':
    app.run(debug=True)

    



