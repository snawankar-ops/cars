class Cars:
    pay_rate = 0.8 #after 20% discount
    def __init__(self, make: str, model: str, price:float):

        self.make = make
        self.model = model
        self.__price = price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def get_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Price: {self.__price}")

#adding a getter
    def get_price(self):
        return self.__price
    
#adding a setter
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("price cannot be negative")

car1 = Cars("Toyota", "corolla", 100000)
car2 = Cars("Ford", "Mustang", 200000)

car1.apply_discount()
car2.apply_discount()

car1.get_info()
car2.get_info()

#get price

print(car1.get_price())

#set price
car1.set_price(9000)

#confirming change
car1.get_info()

#creating a subclass electriccar

class ElectricCar(Cars):
    #adding battery range
    def __init__(self, make:str, model:str, price:float, battery_range:float):
        super().__init__(make, model, price)
        self.battery_range = battery_range

    def get_info(self):
        super().get_info()
        print(f"battery range: {self.battery_range} miles")

e1 = ElectricCar("tesla", "modelxyz", 50000, 23)
e1.get_info()

#creating a subclass sportscar

class SportsCar(Cars):
    def __init__(self, make:str, model:str, price:float, top_speed:float):
        super().__init__(make, model, price)
        self.top_speed = top_speed

    def get_info(self):
        super().get_info()
        print(f"top speed is {self.top_speed} mph")

s1 = SportsCar("porsche", "modelblabla", 900000, 78)
s1.get_info()

    
