#!/usr/bin/python
# Benjamin Wiens
# Vending Machine with Change Code (Return Change)

import random
class Random_Vending_Machine:
    def __init__(self):
        self.amount = 0
        self.items = ['Fanta', 'Coke', 'Pepsi']
    def show_items(self):
        for item in self.items:
            print(item)
    def buy_item(self):
        if self.amount - 1 < 1.25:
            print("Add more credits.")
        else:
            self.amount -= 1.25
        print("Please enjoy your ", random.choice(self.items))
        print("Credits: ", self.amount)
    def add_items(self, newitem):
        self.items.append(newitem)
    def insert_money(self, money):
        self.amount += money
        print("Credit: ", self.amount)
    def return_change(self):
        self.result = []
        self.change = [10,5,1,0.25]
        while self.amount != 0:
            for i in self.change:
                if self.amount == 0:
                    break
                else:
                    while self.amount - i >= 0:
                        self.result.append(i)
                        self.amount -= i
        return self.result

    #def return_change(self):
     #   change =

newmachine = Random_Vending_Machine()
newmachine.show_items()
newmachine.add_items('Mountain Dew')
newmachine.show_items()
newmachine.insert_money(100)
newmachine.buy_item()
newmachine.buy_item()
print(newmachine.return_change())
