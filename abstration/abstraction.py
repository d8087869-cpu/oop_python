#1
from abc import ABC, abstractmethod

class DeliveryMetod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
class BikeDelivery(DeliveryMetod):
    def deliver(self, order_id):
        return (f'order {order_id} deliverd by bike')
bike = BikeDelivery()
print(bike.deliver(101))

#2

from abc import ABC, abstractmethod
class DeliveryMetod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass

class DroneDelivery(DeliveryMetod):
    def deliver(self, order_id):
        return (f'order {order_id} deliverd by drone at your door.')
    
class CarDelivery(DeliveryMetod):
    def deliver(self, order_id):
        return (f'order {order_id} brought to your bilding by car.')
drone = DroneDelivery()
car = CarDelivery()
print(car.deliver(202))
print(drone.deliver(202))

#3 
from abc import ABC, abstractmethod
class DeliveryMethod(ABC):
    def __init__(self,company_name):
        self.companey_name = company_name
    def deliver(self,order_id):
        pass
class BikeDelivery(DeliveryMethod):
    def __init__(self, company_name):
        super().__init__(company_name)
    def deliver(self,order_id):
        return(f'[{self.companey_name}] order {order_id} - bike delivery ')
class DroneDelivery(DeliveryMethod):
    def __init__(self, company_name):
        super().__init__(company_name)
    def deliver(self, order_id):
        return (f"[{self.companey_name}] Order {order_id} — drone delivery.")
bike = BikeDelivery('speedRiders')
drone= DroneDelivery(" SkyEx")
print(bike.deliver(303))
print(drone.deliver(303))

#4 
from abc import ABC,abstractmethod
class DeliveryMetod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
    def get_eta(self):
        pass
class BikerDelivery(DeliveryMetod):
    def deliver(self, order_id):
        return (f"Order {order_id} delivered by bike.")
    def get_eta(self):
        return 30
class DroneDelivery(DeliveryMetod):
    def deliver(self, order_id):
        return (f'order {order_id} deliverd by drone')
    def get_eta(self):
        return 15
bike = BikerDelivery()
print(bike.deliver(1))
print(f'ETA: {bike.get_eta()} minutes')

drone = DroneDelivery()
print(drone.deliver(1))
print(f'ETA: {drone.get_eta()} minutes')

#5
from abc import ABC,abstractmethod
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
class BrokenDelivery(DeliveryMethod):
    pass
#broken = BrokenDelivery()
class FixDelivery(DeliveryMethod):
    def deliver(self, order_id):
        return (f'order {order_id} was deliverd by fixed ')
fixed = FixDelivery()
print(fixed.deliver(5))

#6
class DeliveryFee:
    @staticmethod
    def calculate(distance_km, rate_per_km):
        return distance_km * rate_per_km

    @staticmethod
    def with_surcharge(base_fee, surcharge_percent):
        return base_fee * (1 + surcharge_percent / 100)

    @staticmethod
    def is_free(distance_km):
        if distance_km <= 2.0:
            return True
        else:
            return False
print(DeliveryFee.calculate(5, 3.0))
print(DeliveryFee.with_surcharge(15.0, 10))
print(DeliveryFee.is_free(1.5))

#7
from abc import ABC, abstractmethod


class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self, order_id):
        pass

    @abstractmethod
    def get_eta(self):
        pass

class WalkingDelivery(DeliveryMethod):
    def deliver(self, order_id):
        return f"Order {order_id} delivered by walking."
    def get_eta(self):
        return 60
    
class ExpressDelivery(DeliveryMethod):
    def deliver(self, order_id):
        return f"Order {order_id} delivered by express."
    def get_eta(self):
        return 10
    
class DeliveryHelper:
    @staticmethod
    def faster(d1, d2):
        if d1.get_eta() < d2.get_eta():
            return d1
        else:
            return d2

walking = WalkingDelivery()
express = ExpressDelivery()

faster_option = DeliveryHelper.faster(walking, express)
print(f"Faster option: {faster_option.__class__.__name__}")

#8
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

class PushNotifier(Notifier):
    def send(self, recipient, message):
        return f"Push to {recipient}: {message}"

class WhatsAppNotifier(Notifier):
    def send(self, recipient, message):
        return f"WhatsApp to {recipient}: {message}"

class InAppNotifier(Notifier):
    def send(self, recipient, message):
        return f"In-app banner for {recipient}: {message}"

notifiers = [PushNotifier(), WhatsAppNotifier(), InAppNotifier()]
for notifier in notifiers:
    print(notifier.send("customer_42", "Your order is on the way!"))

#9
from abc import ABC, abstractmethod

class Restaurant(ABC):
    @abstractmethod
    def get_menu(self):
        pass

    @abstractmethod
    def prepare_order(self, item_name):
        pass

class ItalianRestaurant(Restaurant):
    def get_menu(self):
        return ['pasta', 'pizza', 'tiramisu']
    def prepare_order(self, item_name):
        print(f"Preparing {item_name} the Italian way.")

class SushiRestaurant(Restaurant):
    def get_menu(self):
        return ['maki', 'nigiri', 'ramen']
    def prepare_order(self, item_name):
        print(f"Preparing {item_name} in Japanese style.")

class BurgerJoint(Restaurant):
    def get_menu(self):
        return ['burger', 'fries', 'shake']
    def prepare_order(self, item_name):
        print(f"Grilling up a {item_name} , fast food style.")

restaurants = [ItalianRestaurant(), SushiRestaurant(), BurgerJoint()]
for restaurant in restaurants:
    print(restaurant.get_menu())
    restaurant.prepare_order(restaurant.get_menu()[0])

#10

from abc import ABC, abstractmethod

class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self, order_id):
        pass

    @abstractmethod
    def get_eta(self):
        pass

    @abstractmethod
    def get_cost(self, distance_km):
        pass

class BikeDelivery(DeliveryMethod):
    def deliver(self, order_id):
        return f"Order {order_id} delivered by bike."

    def get_eta(self):
        return 30

    def get_cost(self, distance_km):
        return distance_km * 1.0

class DroneDelivery(DeliveryMethod):
    def deliver(self, order_id):
        return f"Order {order_id} dropped by drone at your door."

    def get_eta(self):
        return 15

    def get_cost(self, distance_km):
        return distance_km * 2.5

class CarDelivery(DeliveryMethod):
    def deliver(self, order_id):
        return f"Order {order_id} brought to your building by car."

    def get_eta(self):
        return 20

    def get_cost(self, distance_km):
        return distance_km * 1.8

class WalkingDelivery(DeliveryMethod):
    def deliver(self, order_id):
        return f"Order {order_id} delivered by walking courier."

    def get_eta(self):
        return 60

    def get_cost(self, distance_km):
        return distance_km * 0.5

class Platform:
    def __init__(self, delivery_methods):
        self.delivery_methods = delivery_methods

    def cheapest_option(self, distance_km):
        cheapest = self.delivery_methods[0]
        for method in self.delivery_methods:
            if method.get_cost(distance_km) < cheapest.get_cost(distance_km):
                cheapest = method
        return cheapest

    def fastest_option(self):
        fastest = self.delivery_methods[0]
        for method in self.delivery_methods:
            if method.get_eta() < fastest.get_eta():
                fastest = method
        return fastest

all_methods = [BikeDelivery(), DroneDelivery(), CarDelivery(), WalkingDelivery()]
platform = Platform(all_methods)

cheapest = platform.cheapest_option(5.0)
fastest = platform.fastest_option()
print(f"Cheapest: {cheapest.__class__.__name__}")
print(f"Fastest: {fastest.__class__.__name__}")