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

