"""
ITN 160
Project 3: Point of Sale System - New

Rashed Khan
11/10/20
"""

from guizero import *

from datetime import datetime

from time import strftime

# from time import time

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


def main():
    def food_order():
        global total_price
        global item_id
        global food
        global food_quantity_str

        # Make a list of current items and convert it to a sting from combo
        food = food_items.value.split()
        food_quantity_str = str(food_quantity.value)

        # Give a item id and add the order to the order window
        item_id += 1
        item_id_str = str(item_id)
        if len(food) == 3:
            lbx_order_windows.append(
                f" {'Item: ' + item_id_str + ' '}{food[0]} {food[1]} {food_quantity_str + '@'} {food[2]} ")
        else:
            lbx_order_windows.append(f" {'Item: ' + item_id_str + ' '}{food[0]}  {food_quantity_str + '@'} {food[1]} ")

        # Remove dollar sign from price and make them float

        choosen_food = food_items.value.split()
        cho_food = float(choosen_food[-1].replace('$', ''))
        make_quantity_int = int(food_quantity.value)

        # Calculate and add them to total price
        calculate = cho_food * make_quantity_int
        total_price = total_price + calculate

        # Reset the combo boxes
        food_items.value = FOOD_NAME[0]
        food_quantity.value = QUANTITY[0]

        # return item_id

    def drink_order():

        global item_id
        global total_price
        global soda
        global soda_quantity_str

        # Make a list of current items and convert it to a sting from combo
        soda = soda_items.value.split()
        soda_quantity_str = str(soda_quantity.value)

        # Give a item id and add the order to the order window
        item_id += 1
        item_id_str = str(item_id)
        if len(soda) == 3:
            lbx_order_windows.append(
                f" {'Item: ' + item_id_str + ' '}{soda[0]} {soda[1]} {soda_quantity_str + '@'} {soda[2]} ")
        else:
            lbx_order_windows.append(f" {'Item: ' + item_id_str + ' '}{soda[0]}  {soda_quantity_str + '@'} {soda[1]} ")

        # Remove dollar sign from price and make them float
        choosen_soda = soda_items.value.split()
        cho_soda = float(choosen_soda[-1].replace('$', ''))
        make_quantity_int = int(soda_quantity.value)

        # Calculate and add them to total price
        calculate = cho_soda * make_quantity_int
        total_price = total_price + calculate

        # Reset the combo boxes
        soda_items.value = SODA_NAME[0]
        soda_quantity.value = QUANTITY[0]

    def submit_order():
        # if item_id != 0:
        global total_price
        global ticket_number

        # add a increment in the ticket number and make it to string
        ticket_number += 1
        ticket_number_str = str(ticket_number)

        # Current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # Add ticket number and current time into the ticket window
        lbx_ticket_window.append(f" {'Ticket: ' + ticket_number_str + ' '}{strftime('%D') + ' '}{current_time} ")

        # Adding items into the order window and also adding total price
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

        # Reset total price
        total_price = 0
        print(total_price)

        # Clear order window
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

            # Update total price by removing the price
            total_price = total_price - removed_price
            print(total_price)

    # Define the screen layout
    app = App(title='Hakone Deluxe', width=660, height=300,
              bg='grey')
    app.text_size = 14

    window1 = Window(app, title='Order Preview', width=450, height=400)
    window2 = Window(app, title='Ticket Window', width=450, height=400)

    Text(app, text="\nEnter your entree and beverage choices\n")
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
    # Text(box_left_2, 'Membership Level  ', align='left')
    food_items = Combo(box_left_2, options=FOOD_NAME, align='left')

    # Food quantity and order pushbutton using a combo in box_left_2
    box_left_3 = Box(box_left, width=200, height=75, border=0)
    food_quantity = Combo(box_left_3, options=QUANTITY, align='left')
    PushButton(box_left_3, text='Order', command=food_order)

    # order preview window text and listbox ======================== window-2
    Text(window1, text='\nClick on a member to remove membership\n')
    lbx_order_windows = ListBox(window1, width=400, height=250, command=remove_member, scrollbar=True)
    lbx_order_windows.font = 'Consolas'
    PushButton(window1, text='Submit Order', command=submit_order)

    # ticket window text and listbox ===================== windows-3
    lbx_ticket_window = ListBox(window2, width=400, height=350, scrollbar=True)  # command=remove_member,
    lbx_ticket_window.font = 'Consolas'

    app.display()


main()
