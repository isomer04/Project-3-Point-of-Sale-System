import mysql.connector
from guizero import *
from datetime import datetime
from time import strftime

FOOD_NAME = ['Chicken Teriyaki $16.99', 'NY Steak $22.99', 'Salmon $18.99', 'Lobster $30.99']
SODA_NAME = ['Coke $2.50', 'Iced Tea $2.50', 'Ginger Ale $3.00', 'Coffee $3.50']
QUANTITY = [1, 2, 3, 4]

item_id = 0
ticket_number = 0
total_price = 0
food = ''
food_quantity_str = ''
soda = ''
soda_quantity_str = ''
customer_name = ''

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="pointofsale"
)

cursor = db.cursor()

def main():


    def create_order(user_id, food, soda, total_price):
        # Convert food and soda lists to strings
        food_str = ', '.join(food)
        soda_str = ', '.join(soda)

        # Insert order into the 'orders' table
        sql = "INSERT INTO orders (user_id, food, soda, total_price) VALUES (%s, %s, %s, %s)"
        val = (user_id, food_str, soda_str, total_price)
        cursor.execute(sql, val)
        db.commit()

    def authenticate_user(username, password):
        # Check if the username and password match a record in the 'users' table
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (username, password)
        cursor.execute(sql, val)
        user = cursor.fetchone()
        return user

    def show_main_window():
        login_window.hide()
        signup_window.hide()
        window1.show()
        window2.show()

    def show_login():
        login_window.show()
        signup_window.hide()
        window1.hide()
        window2.hide()

    def show_signup():
        login_window.hide()
        signup_window.show()
        window1.hide()
        window2.hide()

    def login():
        username = login_username.value
        password = login_password.value
        user = authenticate_user(username, password)
        if user:
            # Login successful, open main app window
            # login_window.hide()
            # app.show()
            show_main_window()

        else:
            error("Login Error", "Invalid username or password")

    def signup():
        username = signup_username.value
        password = signup_password.value
        email = signup_email.value

        # Check if the username already exists
        sql_check = "SELECT * FROM users WHERE username = %s"
        val_check = (username,)
        cursor.execute(sql_check, val_check)
        existing_user = cursor.fetchone()

        if existing_user:
            error("Signup Error", "Username already exists. Please choose a different username.")
        else:
            # Username is unique, proceed with signup
            sql_insert = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
            val_insert = (username, password, email)
            cursor.execute(sql_insert, val_insert)
            db.commit()
            info("Signup Success", "Signup successful! You can now log in.")
            # signup_window.hide()
            # show_main_window()
            show_login()

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

    def submit_order():
        global total_price, ticket_number, food, soda, customer_name

        # Add a separator line between tickets
        lbx_ticket_window.append("-" * 50)

        # Add an increment in the ticket number and make it a string
        ticket_number += 1
        ticket_number_str = str(ticket_number)

        # Current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        # Add the ticket number and current time into the ticket window
        lbx_ticket_window.append(f" {'Ticket: ' + ticket_number_str + ' '}{strftime('%D') + ' '}{current_time} ")
        lbx_ticket_window.append(f" {'Customer: ' + customer_name}")

        # Adding items into the order window and also adding the total price
        if len(food) == 3:
            lbx_ticket_window.append(
                f" {food[0]} {food[1]} {food_quantity_str + '@'} {food[2]} ")
        else:
            lbx_ticket_window.append(f"{food[0]}  {food_quantity_str + '@'} {food[1]} ")

        if len(soda) == 3:
            lbx_ticket_window.append(
                f" {soda[0]} {soda[1]} {soda_quantity_str + '@'} {soda[2]} ")
        else:
            lbx_ticket_window.append(f"{soda[0]}  {soda_quantity_str + '@'} {soda[1]} ")

        lbx_ticket_window.append(f"{'Total: $' + str(total_price)}")

        print(total_price)

        # Save the order in the database
        print(create_order(1, food, soda, total_price))  # Replace 1 with the actual user_id

        # Reset the total price
        total_price = 0
        # name_box.value = ""
        print(total_price)

        # Clear the order window
        lbx_order_windows.clear()

    # Remove a member
    def remove_member(line):
        global total_price
        reply = yesno(title='Hakone Deluxe',
                      text='OK to remove:\n' + line)
        if reply:
            # Split the line the user selected
            removed_item = line.split()
            removed_price = float(removed_item[-1].replace('$', ''))

            # Remove the current line
            lbx_order_windows.remove(line)
            print(total_price)

            # Update the total price by removing the price
            total_price = total_price - removed_price
            print(total_price)

    # Define the screen layout
    app = App(title='Hakone Deluxe', width=660, height=400, bg='grey')
    app.text_size = 14

    login_window = Window(app, title='Login', width=300, height=150, layout="grid")

    Text(login_window, text="Username:", grid=[0, 0], align="left")
    login_username = TextBox(login_window, width=15, grid=[1, 0])
    Text(login_window, text="Password:", grid=[0, 1], align="left")
    login_password = TextBox(login_window, width=15, grid=[1, 1], hide_text=True)
    PushButton(login_window, text="Login", command=login, grid=[1, 2])
    PushButton(login_window, text="Signup", command=show_signup, grid=[1, 3])

    signup_window = Window(app, title='Signup', width=300, height=200, layout="grid")
    Text(signup_window, text="Username:", grid=[0, 0], align="left")
    signup_username = TextBox(signup_window, width=15, grid=[1, 0])
    Text(signup_window, text="Password:", grid=[0, 1], align="left")
    signup_password = TextBox(signup_window, width=15, grid=[1, 1], hide_text=True)
    Text(signup_window, text="Email:", grid=[0, 2], align="left")
    signup_email = TextBox(signup_window, width=15, grid=[1, 2])
    PushButton(signup_window, text="Signup", command=signup, grid=[1, 3])
    PushButton(signup_window, text="Login", command=show_login, grid=[1, 4])

    window1 = Window(app, title='Order Preview', width=450, height=400)
    window2 = Window(app, title='Ticket Window', width=450, height=400)

    # Space on the left border
    Box(app, width=25, height=100, align='left')

    # Left box for foods
    box_left = Box(app, width=280, height=180, border=1, align='left')

    # Space between boxes
    Box(app, width=30, height=100, align='left')

    # Right box for drinks
    box_right = Box(app, width=280, height=200, border=1, align='left')

    # Soda name using a combo in box_right_2
    box_right_2 = Box(box_right, width=260, height=75, border=0)
    soda_items = Combo(box_right_2, options=SODA_NAME, align='left')

    # Soda quantity and order pushbutton using a combo in box_right_2
    box_right_3 = Box(box_right, width=200, height=75, border=0)
    soda_quantity = Combo(box_right_3, options=QUANTITY, align='left')
    PushButton(box_right_3, text='Order', command=drink_order)

    # Food name using a combo in box_left_2
    box_left_2 = Box(box_left, width=260, height=75, border=0)
    food_items = Combo(box_left_2, options=FOOD_NAME, align='left')

    # Food quantity and order pushbutton using a combo in box_left_2
    box_left_3 = Box(box_left, width=200, height=75, border=0)
    food_quantity = Combo(box_left_3, options=QUANTITY, align='left')
    PushButton(box_left_3, text='Order', command=food_order)

    # Order preview window text and listbox ======================== window-2
    Text(window1, text='\nClick on a member to remove membership\n')
    lbx_order_windows = ListBox(window1, width=400, height=250, command=remove_member, scrollbar=True)
    lbx_order_windows.font = 'Consolas'
    PushButton(window1, text='Submit Order', command=submit_order)

    # Ticket window text and listbox ===================== windows-3
    lbx_ticket_window = ListBox(window2, width=400, height=350, scrollbar=True)
    lbx_ticket_window.font = 'Consolas'

    # Initially hide signup and main windows
    signup_window.hide()
    window1.hide()
    window2.hide()

    # Show only the login window initially
    show_login()

    # Run the main function
    app.display()

# Run the main function
main()

# Close the database connection when done
db.close()
