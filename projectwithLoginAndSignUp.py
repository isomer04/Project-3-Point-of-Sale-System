from guizero import *
from datetime import datetime
from time import strftime
import mysql.connector
from mysql.connector import Error

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

def login(username, password):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database_name',
            user='your_username',
            password='your_password'
        )

        # Execute a select query to check if the username and password match
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        # Fetch the result
        result = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        if result:
            # Login successful
            return True
        else:
            # Login failed
            return False

    except Error as e:
        print("Error connecting to MySQL database", e)
        return False

def signup(username, password):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database_name',
            user='your_username',
            password='your_password'
        )

        # Execute an insert query to add a new user
        cursor = connection.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))

        # Commit the changes and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        # Signup successful
        return True

    except Error as e:
        print("Error connecting to MySQL database", e)
        return False

def main():
    def food_order():
        global total_price
        global item_id
        global food
        global food_quantity_str

        # Rest of the code...

    def drink_order():
        global item_id
        global total_price
        global soda
        global soda_quantity_str

        # Rest of the code...

    def submit_order():
        global total_price
        global ticket_number

        # Rest of the code...

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

            # Update total price by removing the price
            total_price = total_price - removed_price
            print(total_price)
            
            
            

    app = App(title='Hakone Deluxe', width=660, height=300, bg='grey')
    app.text_size = 14

    window1 = Window(app, title='Order Preview', width=450, height=400)
    window2 = Window(app, title='Ticket Window', width=450, height=400)

    Text(app, text="\nEnter your entree and beverage choices\n")
    # Rest of the code...


    main()
