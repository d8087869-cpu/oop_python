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