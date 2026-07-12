#1
class Menuitem:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def describe(self):
        print(f'item: {self.name} , price: {self.price} ')   
menu1 =Menuitem ('Espresso' , 3.5)
menu1.describe()
#2
class Customer:
    def __init__(self,name,fav_drink):
        self.name = name
        self.fav_drink = fav_drink
    def greet(self):
        print(f'Hi! I am {self.name}, and I would like a {self.fav_drink}')
customer1 = Customer ('alice' , 'Latte') 
customer1.greet()      
#3
class Menuitem:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def describe(self):
        print(f'item: {self.name} , price: {self.price} ')   
menu1 =Menuitem('Latte', 3.5)
menu2 = Menuitem('Croissant' , 2.0)
menu3 = Menuitem('Cold Brew' , 5.0)
menu1.describe()
menu2.describe()
menu3.describe()