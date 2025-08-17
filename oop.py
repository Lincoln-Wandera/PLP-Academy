class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"Device: {self.brand} {self.model}"


# Child class 
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # call parent constructor
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}")
    
    def charge(self):
        print(f"Charging {self.model}. Battery now at {self.battery}%.")

    # Encapsulation (
    def get_storage(self):
        return self.storage

    def set_storage(self, new_storage):
        self.storage = new_storage


# objects
phone1 = Smartphone("Apple", "iPhone 14", "128GB", 85)
phone2 = Smartphone("Samsung", "Galaxy S23", "256GB", 65)

# methods
print(phone1.device_info())
phone1.make_call("123-456-789")
phone1.charge()
print(f"Storage before upgrade: {phone1.get_storage()}")
phone1.set_storage("256GB")
print(f"Storage after upgrade: {phone1.get_storage()}")

# Polymorphism
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement move()")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("Flying ")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water")

# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move() 