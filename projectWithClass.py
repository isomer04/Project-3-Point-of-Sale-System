import mysql.connector
from guizero import App, Box, Combo, PushButton, Text, TextBox, yesno, ListBox
from datetime import datetime
from time import strftime

class PointOfSaleApp:
    def __init__(self):
        self.item_id = 0
        self.ticket_number = 0
        self.total_price = 0
        self.food = ''
        self.food_quantity_str = ''
        self.soda = ''
        self.soda_quantity_str = ''
        self.customer_name = ''

        # Connect to MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="pointofsale"
        )
        self.cursor = self.db.cursor()

        self.create_gui()

    def create_gui(self):
        self.app = App(title='Login', width=300, height=150, layout="grid")

        # Other GUI components initialization here...

        self.login_window = App(title='Login', width=300, height=150, layout="grid")
        # GUI components related to login_window...
        Text(self.login_window, text="Username:", grid=[0, 0], align="left")
        TextBox(self.login_window, width=15, grid=[1, 0], name="login_username")
        Text(self.login_window, text="Password:", grid=[0, 1], align="left")
        TextBox(self.login_window, width=15, grid=[1, 1], hide_text=True, name="login_password")
        PushButton(self.login_window, text="Login", command=self.login, grid=[1, 2])
        PushButton(self.login_window, text="Signup", command=self.show_signup, grid=[1, 3])

        self.signup_window = App(title='Signup', width=300, height=200, layout="grid")
        # GUI components related to signup_window...
        Text(self.signup_window, text="Username:", grid=[0, 0], align="left")
        TextBox(self.signup_window, width=15, grid=[1, 0], name="signup_username")
        Text(self.signup_window, text="Password:", grid=[0, 1], align="left")
        TextBox(self.signup_window, width=15, grid=[1, 1], hide_text=True, name="signup_password")
        Text(self.signup_window, text="Email:", grid=[0, 2], align="left")
        TextBox(self.signup_window, width=15, grid=[1, 2], name="signup_email")
        PushButton(self.signup_window, text="Signup", command=self.signup, grid=[1, 3])
        PushButton(self.signup_window, text="Login", command=self.show_login, grid=[1, 4])

        self.window1 = App(title='Order Preview', width=450, height=400)
        # GUI components related to window1...
        Text(self.window1, text='\nClick on a member to remove membership\n')
        ListBox(self.window1, width=400, height=250, command=self.remove_member, scrollbar=True, name="lbx_order_windows").font = 'Consolas'
        PushButton(self.window1, text='Submit Order', command=self.submit_order)

        self.window2 = App(title='Ticket Window', width=450, height=400)
        # GUI components related to window2...
        ListBox(self.window2, width=400, height=350, scrollbar=True, name="lbx_ticket_window").font = 'Consolas'

        self.show_login()

    def show_login(self):
        self.login_window.show()
        self.signup_window.hide()
        self.window1.hide()
        self.window2.hide()

    def show_signup(self):
        self.login_window.hide()
        self.signup_window.show()
        self.window1.hide()
        self.window2.hide()

    def show_main_window(self):
        self.login_window.hide()
        self.signup_window.hide()
        self.window1.show()
        self.window2.show()

    def login(self):
        username = self.login_window["login_username"].value
        password = self.login_window["login_password"].value
        user = self.authenticate_user(username, password)
        if user:
            self.show_main_window()
        else:
            # Error handling for invalid login
            pass

    def signup(self):
        username = self.signup_window["signup_username"].value
        password = self.signup_window["signup_password"].value
        email = self.signup_window["signup_email"].value

        # Check if the username already exists
        existing_user = self.check_existing_user(username)

        if existing_user:
            # Error handling for existing username
            pass
        else:
            self.create_user(username, password, email)
            # Info message for successful signup
            pass

    def authenticate_user(self, username, password):
        # Check if the username and password match a record in the 'users' table
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (username, password)
        self.cursor.execute(sql, val)
        user = self.cursor.fetchone()
        return user

    def check_existing_user(self, username):
        # Check if the username already exists in the 'users' table
        sql_check = "SELECT * FROM users WHERE username = %s"
        val_check = (username,)
        self.cursor.execute(sql_check, val_check)
        existing_user = self.cursor.fetchone()
        return existing_user

    def create_user(self, username, password, email):
        # Insert new user into the 'users' table
        sql_insert = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        val_insert = (username, password, email)
        self.cursor.execute(sql_insert, val_insert)
        self.db.commit()

    def food_order():
        global total_price, item_id, food, food_quantity_str

        # Make a list of current items and convert it to a string from combo
        food = food_items.value.split()
        food_quantity_str = str(food_quantity.value)

        # Give an item id and add the order to the order window
        item_id += 1
        item_id_str = str(item_id)
        if len(food) == 3:
            lbx_order_windows.append(
                f" {'Item: ' + item_id_str + ' '}{food[0]} {food[1]} {food_quantity_str + '@'} {food[2]} ")
        else:
            lbx_order_windows.append(f" {'Item: ' + item_id_str + ' '}{food[0]}  {food_quantity_str + '@'} {food[1]} ")

        # Remove the dollar sign from the price and make them float
        chosen_food = food_items.value.split()
        cho_food = float(chosen_food[-1].replace('$', ''))
        make_quantity_int = int(food_quantity.value)

        # Calculate and add them to the total price
        calculate = cho_food * make_quantity_int
        total_price = total_price + calculate

        # Reset the combo boxes
        food_items.value = FOOD_NAME[0]
        food_quantity.value = QUANTITY[0]

    def drink_order():
        global item_id, total_price, soda, soda_quantity_str

        # Make a list of current items and convert it to a string from combo
        soda = soda_items.value.split()
        soda_quantity_str = str(soda_quantity.value)

        # Give an item id and add the order to the order window
        item_id += 1
        item_id_str = str(item_id)
        if len(soda) == 3:
            lbx_order_windows.append(
                f" {'Item: ' + item_id_str + ' '}{soda[0]} {soda[1]} {soda_quantity_str + '@'} {soda[2]} ")
        else:
            lbx_order_windows.append(f" {'Item: ' + item_id_str + ' '}{soda[0]}  {soda_quantity_str + '@'} {soda[1]} ")

        # Remove the dollar sign from the price and make them float
        chosen_soda = soda_items.value.split()
        cho_soda = float(chosen_soda[-1].replace('$', ''))
        make_quantity_int = int(soda_quantity.value)

        # Calculate and add them to the total price
        calculate = cho_soda * make_quantity_int
        total_price = total_price + calculate

        # Reset the combo boxes
        soda_items.value = SODA_NAME[0]
        soda_quantity.value = QUANTITY[0]

    def submit_order(self):
        # Add a separator line between tickets
        self.window2["lbx_ticket_window"].append("-" * 50)

        # Add an increment in the ticket number and make it a string
        self.ticket_number += 1
        ticket_number_str = str(self.ticket_number)

        # Current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        # Add the ticket number and current time into the ticket window
        self.window2["lbx_ticket_window"].append(f" {'Ticket: ' + ticket_number_str + ' '}{strftime('%D') + ' '}{current_time} ")
        self.window2["lbx_ticket_window"].append(f" {'Customer: ' + self.customer_name}")

        # Adding items into the order window and also adding the total price
        if len(self.food) == 3:
            self.window2["lbx_ticket_window"].append(
                f" {self.food[0]} {self.food[1]} {self.food_quantity_str + '@'} {self.food[2]} ")
        else:
            self.window2["lbx_ticket_window"].append(f"{self.food[0]}  {self.food_quantity_str + '@'} {self.food[1]} ")

        if len(self.soda) == 3:
            self.window2["lbx_ticket_window"].append(
                f" {self.soda[0]} {self.soda[1]} {self.soda_quantity_str + '@'} {self.soda[2]} ")
        else:
            self.window2["lbx_ticket_window"].append(f"{self.soda[0]}  {self.soda_quantity_str + '@'} {self.soda[1]} ")

        self.window2["lbx_ticket_window"].append(f"{'Total: $' + str(self.total_price)}")

        # Save the order in the database
        self.create_order(1, self.food, self.soda, self.total_price)  # Replace 1 with the actual user_id

        # Reset the total price
        self.total_price = 0
        self.food_items.value = FOOD_NAME[0]
        self.food_quantity.value = QUANTITY[0]
        self.soda_items.value = SODA_NAME[0]
        self.soda_quantity.value = QUANTITY[0]

        # Clear the order window
        self.window1["lbx_order_windows"].clear()

    def create_order(self, user_id, food, soda, total_price):
        # Convert food and soda lists to strings
        food_str = ', '.join(food)
        soda_str = ', '.join(soda)

        # Insert order into the 'orders' table
        sql = "INSERT INTO orders (user_id, food, soda, total_price) VALUES (%s, %s, %s, %s)"
        val = (user_id, food_str, soda_str, total_price)
        self.cursor.execute(sql, val)
        self.db.commit()

    def remove_member(self, line):
        # Remove a member logic here...
        reply = yesno(title='Hakone Deluxe', text='OK to remove:\n' + line)
        if reply:
            # Split the line the user selected
            removed_item = line.split()
            removed_price = float(removed_item[-1].replace('$', ''))

            # Remove the current line
            self.window1["lbx_order_windows"].remove(line)

            # Update the total price by removing the price
            self.total_price = self.total_price - removed_price

#... (remaining code)



if __name__ == "__main__":
    pos_app = PointOfSaleApp()
    pos_app.main()