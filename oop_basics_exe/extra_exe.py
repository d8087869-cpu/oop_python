'''
#1
class MenuItem:
    def __init__(self,name ,price,category):
        self.name = name
        self.price = price
        self.category = category
    def is_drink(self):
        if 'drink' in self.category:
            return True
        else:
            return False
        
    def is_cheap(self,limit):
        if self.price < limit:
            return True
        else:
            return False
item1 =MenuItem('Espresso',3.5,'hot drink') 
item2 =MenuItem('Cold Coffe',4.5,'cold drink')
item3 =MenuItem('Muffin',2.0,'food')
item4 =MenuItem('sandwich',6.0,'food') 
items =[item1,item2,item3,item4] 
for item in items:
    print(item.name)
    print("is_drink():", item.is_drink())
    print("is_cheap(3.0):", item.is_cheap(3.0))
    print()
'''
#2
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.points = 0
    def purchase(self, item_name, price):
        if price <= self.balance:
            self.balance = self.balance - price
            self.points = self.points + 10
        else:
            print(f"Not enough balance for {item_name}.")
    def redeem(self):
        if self.points >= 50:
            self.balance = self.balance + 5.0
            self.points = 0
    def status(self):
        print(f"Name: {self.name} | Balance: ${self.balance} | Points: {self.points}")

noa = Customer("Noa", 15.0)
noa.status()

noa.purchase("Coffee", 3.0)
noa.status()
noa.redeem()
noa.status()

#3
class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items
    def total_prep_time(self):
        total = 0
        for name, minutes in self.items:
            total = total + minutes
        return total
    def ready_by(self, minutes):
        if self.total_prep_time() <= minutes:
            return True
        else:
            return False
    def print_order(self):
        for name, minutes in self.items:
            print(f"{name} - {minutes} min")
    def slowest_item(self):
        slowest_name = self.items[0][0]
        slowest_time = self.items[0][1]
        for name, minutes in self.items:
            if minutes > slowest_time:
                slowest_time = minutes
                slowest_name = name

        return slowest_name
order = Order("Moshe", [("Latte", 3), ("Sandwich", 7), ("Smoothie", 5)])
order.print_order()
print("Total prep:", order.total_prep_time(), "min")
print("ready_by(10):", order.ready_by(10))
print("ready_by(20):", order.ready_by(20))
print("Slowest:", order.slowest_item())