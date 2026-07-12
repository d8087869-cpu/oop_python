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
'''

#4 
class CoffeeShop:
    def __init__(self, name):
        self.name = name
        self.revenue = 0.0
    def sell(self, item_name, price):
        self.revenue = self.revenue + price
        print(f"Sold {item_name} for ${price}")

    def sell_discounted(self, item_name, price, discount):
        discounted_price = price * (1 - discount)
        self.revenue = self.revenue + discounted_price
        print(f"Sold {item_name} for ${discounted_price} (discounted)")

    def daily_summary(self):
        print(f"{self.name} | Daily revenue: ${self.revenue:.2f}")

shop = CoffeeShop("The Bean")
shop.sell("Latte", 3.5)
shop.sell("Muffin", 2.0)
shop.sell("Espresso", 3.0)
shop.sell_discounted("Cappuccino", 4.0, 0.1)  
shop.sell_discounted("Sandwich", 5.0, 0.2)   
shop.daily_summary()

#5
class Drink:
    def __init__(self, name, base_price, size):
        self.name = name
        self.base_price = base_price
        self.size = size
    def final_price(self):
        if self.size == "small":
            return self.base_price
        elif self.size == "medium":
            return self.base_price * 1.3
        elif self.size == "large":
            return self.base_price * 1.6
    def describe(self):
        print(f"{self.name} ({self.size}) -> ${self.final_price():.2f}")
small_latte = Drink("Latte", 3.0, "small")
medium_latte = Drink("Latte", 3.0, "medium")
large_latte = Drink("Latte", 3.0, "large")
small_latte.describe()
medium_latte.describe()
large_latte.describe()
#6
class Shift:
    def __init__(self, barista_name,start_hour,end_hour,drinks_target):
        self.barista_name = barista_name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.drinks_target = drinks_target
    def duration(self):
        return self.end_hour - self.start_hour

    def drinks_per_hour(self):
        return self.drinks_target // self.duration()

    def is_long_shift(self):
        if self.duration() > 6:
            return True
        else:
            return False
    def describe(self):
        print(f"Barista: {self.barista_name} | Hours: {self.duration()} | Target: {self.drinks_target} | Per hour: {self.drinks_per_hour()} | Long shift: {self.is_long_shift()}")
shift1 = Shift("Lior", 8, 16, 120)
shift1.describe()

shift2 = Shift("Dana", 9, 13, 40)
shift2.describe()