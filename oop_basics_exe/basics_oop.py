'''
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
#4
class Customers:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def can_afford(self, price):
        if self.balance >= price:
            return True
        else:
            return False
Customer2 = Customers('Bob',10.0)
print(Customer2.can_afford(12))
#5
class Menuitem:
    def __init__(self,name,price,in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock
    def sell(self):
            self.in_stock = False
    def restock(self):
        self.in_stock = True
    def status(self):
        if self.in_stock:
            print(f'{self.name} is in stock')
        else:
            print(f'{self.name} is sold out')
item = Menuitem("Muffin", 2.5, True)
item.status()
item.sell()
item.status()
item.restock()
item.status()           
#6
class Coffe_shop:
    def __init__(self,name,city,capacity):
        self.name = name
        self.city = city
        self.capacity = capacity
        self.is_open = False
    def open_shop(self): 
        if not self.is_open :
            self.is_open == True
            print(f'{self.name} is now open in {self.city}! capasity {self.capacity} seats.')
        else:
            print(f'{self.is_open} is alrady open')
    def close_shop(self):
        if  self.is_open:
            print(f'{self.name} is alredy closed. see you tomorrow!')
        else:
            self.is_open=False
            print(f'{self.name} is closed. see you tomorrow!')
shop_info = Coffe_shop('Brew House' , 'Tel Aviv' , 40)
shop_info.open_shop()
shop_info.close_shop()
#7
class Menu_item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.order_count = 0
    def order(self):
            self.order_count +=1
            print(f'{self.name} orderd. total orders: {self.order_count}')
item = Menu_item('Cappucciono' ,4.0)
item.order() 
item.order()
item.order()
'''
#8
class Order:
    def __init__(self,customer_name,items):
        self.customer_name = customer_name
        self.items = items
    def item_count(self):
        return len(self.items)
    def print_order(self):
        print(f'order for: {self.customer_name}')
        print(f'items: {self.item_count()}')
        for item in self.items:
            print('-',item)
orders = Order('Dana',['Latte','Croissant','OJ'])
orders.item_count()
orders.print_order()
            