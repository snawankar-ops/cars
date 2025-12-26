class Cars:
    pay_rate = 0.8 #after 20% discount
    def __init__(self, make: str, model: str, price:float):

        assert price>=0 , f"price {price} is not greater than or equal to zero"

        self.make = make
        self.model = model
        self.price = price

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def get_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")

car1 = Cars("Toyota", "corolla", 100000)
car2 = Cars("Ford", "Mustang", 200000)

car1.apply_discount()
car2.apply_discount()

car1.get_info()
car2.get_info()

print(f"The price of car1 is, {car1.price}")
print(f"the price of car2 is, {car2.price}")