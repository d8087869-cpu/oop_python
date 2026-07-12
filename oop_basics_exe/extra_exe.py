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
#7
class MenuItem:
    def __init__(self, name,price):
        self.name = name
        self.price = price
class HappyHour:
    def __init__(self, start_hour,end_hour,discount_percent):
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.discount_percent = discount_percent
    def is_active(self, current_hour):
        if self.start_hour <= current_hour < self.end_hour:
            return True
        else:
            return False

    def discounted_price(self, item):
        return item.price * (1 - self.discount_percent / 100)
beer = MenuItem("Beer", 20.0)
happy_hour = HappyHour(16, 18, 20)
print("is_active(17):", happy_hour.is_active(17))
print("discounted_price:", happy_hour.discounted_price(beer))
print("is_active(19):", happy_hour.is_active(19))
'''

'''
#8
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Combo:
    def __init__(self, name, items, discount):
        self.name = name
        self.items = items
        self.discount = discount
    def original_price(self):
        total = 0
        for item in self.items:
            total = total + item.price
        return total
    def combo_price(self):
        return self.original_price() * (1 - self.discount)
    def savings(self):
        return self.original_price() - self.combo_price()

    def describe(self):
        print(f"{self.name} | Original: ${self.original_price()} | Combo: ${self.combo_price()} | Savings: ${self.savings()}")
espresso = MenuItem("Espresso", 3.5)
croissant = MenuItem("Croissant", 2.5)
breakfast_combo = Combo("Breakfast", [espresso, croissant], 0.1)
breakfast_combo.describe()

#9
class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
class Menu:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def find_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None
    def filter_by_category(self, category):
        result = []
        for item in self.items:
            if item.category == category:
                result.append(item)
        return result

    def cheapest(self):
        cheapest_item = self.items[0]
        for item in self.items:
            if item.price < cheapest_item.price:
                cheapest_item = item
        return cheapest_item
    def most_expensive(self):
        most_expensive_item = self.items[0]
        for item in self.items:
            if item.price > most_expensive_item.price:
                most_expensive_item = item
        return most_expensive_item
    def average_price(self):
        total = 0
        for item in self.items:
            total = total + item.price
        return total / len(self.items)
menu = Menu()
menu.add_item(MenuItem("Espresso", 3.5, "hot drink"))
menu.add_item(MenuItem("Iced tea", 2.5, "cold drink"))
menu.add_item(MenuItem("Muffin", 2.0, "food"))
menu.add_item(MenuItem("Sandwich", 5.0, "food"))
menu.add_item(MenuItem("Latte", 4.0, "hot drink"))

found = menu.find_by_name("Latte")
if found is not None:
    print("Found:", found.name)
else:
    print("Not found")

not_found = menu.find_by_name("Pizza")
print("Search for Pizza:", not_found)

hot_drinks = menu.filter_by_category("hot drink")
print("Hot drinks:")
for item in hot_drinks:
    print(" -", item.name)
    
print("Cheapest:", menu.cheapest().name)
print("Most expensive:", menu.most_expensive().name)

print("Average price:", menu.average_price())
'''
class Table:
    def __init__(self, table_number, seats):
        self.table_number = table_number
        self.seats = seats
        self.is_occupied = False
        self.current_order = None

    def seat_customers(self, count):
        if self.is_occupied:
            print(f"Table {self.table_number} is already occupied.")
        elif count > self.seats:
            print(f"Cannot seat {count} at Table {self.table_number} (only {self.seats} seats).")
        else:
            self.is_occupied = True
            print(f"Table {self.table_number} | Seated {count}")

    def take_order(self, order_text):
        if self.is_occupied:
            self.current_order = order_text
            print(f"Order taken: {order_text}")
        else:
            print("No customers seated.")

    def bill_out(self):
        print(f"Bill for Table {self.table_number}: {self.current_order}")
        self.is_occupied = False
        self.current_order = None
    def status(self):
        print(f"Table {self.table_number} | Seats: {self.seats} | Occupied: {self.is_occupied} | Order: {self.current_order}")
table3 = Table(3, 4)

table3.seat_customers(3)
table3.status()

table3.take_order("2 lattes")
table3.status()

table3.bill_out()
table3.status()
table3.seat_customers(5)