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