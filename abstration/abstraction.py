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