from guizero import App, Text, Box, Combo, PushButton, ListBox, Window, yesno
from datetime import datetime

class PointOfSaleSystem:
    def __init__(self):
        self.FOOD_NAME = ['Chicken Teriyaki $16.99', 'NY Steak $22.99', 'Salmon $18.99', 'Lobster $30.99']
        self.SODA_NAME = ['Coke $2.50', 'Iced Tea $2.50', 'Ginger Ale $3.00', 'Coffee $3.50']
        self.QUANTITY = [1, 2, 3, 4]

        self.item_id = 0
        self.ticket_number = 0
        self.total_price = 0
        self.food = ''
        self.food_quantity_str = ''
        self.soda = ''
        self.soda_quantity_str = ''

    def order(self, item_combo, quantity_combo, lbx_order_windows, item_type):
        item_id_str = str(self.item_id)
        selected_item = item_combo.value.split()
        item_quantity_str = str(quantity_combo.value)

        if len(selected_item) == 3:
            lbx_order_windows.append(f" {'Item: ' + item_id_str + ' '}{selected_item[0]} {selected_item[1]} {item_quantity_str + '@'} {selected_item[2]} ")
        else:
            lbx_order_windows.append(f" {'Item: ' + item_id_str + ' '}{selected_item[0]}  {item_quantity_str + '@'} {selected_item[1]} ")

        chosen_item = item_combo.value.split()
        item_price = float(chosen_item[-1].replace('$', ''))
        quantity = int(quantity_combo.value)

        calculate = item_price * quantity
        self.total_price += calculate

        item_combo.value = item_type[0]
        quantity_combo.value = self.QUANTITY[0]

    def food_order(self):
        self.order(self.food_items, self.food_quantity, self.lbx_order_windows, self.FOOD_NAME)

    def drink_order(self):
        self.order(self.soda_items, self.soda_quantity, self.lbx_order_windows, self.SODA_NAME)

    def submit_order(self):
        self.ticket_number += 1
        ticket_number_str = str(self.ticket_number)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        self.lbx_ticket_window.append(f" {'Ticket: ' + ticket_number_str + ' '}{now.strftime('%D') + ' '}{current_time} ")


        if len(self.food) == 3:
            self.lbx_ticket_window.append(f" {self.food[0]} {self.food[1]} {self.food_quantity_str + '@'} {self.food[2]} ")
        else:
            self.lbx_ticket_window.append(f"{self.food[0]}  {self.food_quantity_str + '@'} {self.food[1]} ")

        if len(self.soda) == 3:
            self.lbx_ticket_window.append(f" {self.soda[0]} {self.soda[1]} {self.soda_quantity_str + '@'} {self.soda[2]} ")
        else:
            self.lbx_ticket_window.append(f"{self.soda[0]}  {self.soda_quantity_str + '@'} {self.soda[1]} ")

        self.lbx_ticket_window.append(f"{'Total: $' + str(self.total_price)}")

        self.total_price = 0
        self.lbx_order_windows.clear()

    def remove_member(self, line):
        reply = yesno(title='Hakone Deluxe', text='OK to remove:\n' + line)
        if reply:
            removed_item = line.split()
            removed_price = float(removed_item[-1].replace('$', ''))
            self.lbx_order_windows.remove(line)
            self.total_price -= removed_price

    def main(self):
        app = App(title='Hakone Deluxe', width=660, height=300, bg='grey')
        app.text_size = 14

        window1 = Window(app, title='Order Preview', width=450, height=400)
        window2 = Window(app, title='Ticket Window', width=450, height=400)

        Text(app, text="\nEnter your entree and beverage choices\n")
        Box(app, width=25, height=100, align='left')

        box_left = Box(app, width=280, height=180, border=1, align='left')
        Box(app, width=30, height=100, align='left')

        box_right = Box(app, width=280, height=200, border=1, align='left')
        box_right_2 = Box(box_right, width=260, height=75, border=0)
        
        self.soda_items = Combo(box_right_2, options=self.SODA_NAME, align='left')
        box_right_3 = Box(box_right, width=200, height=75, border=0)

        self.soda_quantity = Combo(box_right_3, options=self.QUANTITY, align='left')
        PushButton(box_right_3, text='Order', command=self.drink_order)

        box_left_2 = Box(box_left, width=260, height=75, border=0)
        self.food_items = Combo(box_left_2, options=self.FOOD_NAME, align='left')

        box_left_3 = Box(box_left, width=200, height=75, border=0)
        self.food_quantity = Combo(box_left_3, options=self.QUANTITY, align='left')
        PushButton(box_left_3, text='Order', command=self.food_order)

        Text(window1, text='\nClick on a member to remove membership\n')
        self.lbx_order_windows = ListBox(window1, width=400, height=250, command=self.remove_member, scrollbar=True)
        self.lbx_order_windows.font = 'Consolas'
        PushButton(window1, text='Submit Order', command=self.submit_order)

        self.lbx_ticket_window = ListBox(window2, width=400, height=350, scrollbar=True)
        self.lbx_ticket_window.font = 'Consolas'

        app.display()

# Instantiate and run the PointOfSaleSystem
pos_system = PointOfSaleSystem()
pos_system.main()
