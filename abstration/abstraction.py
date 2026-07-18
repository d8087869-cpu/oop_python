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
