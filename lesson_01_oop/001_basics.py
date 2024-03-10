class Vehicle:
    # static members

    year = 2024
    AWS_USERNAME = "user"

    def __init__(self, brand: str, price: float = 350.56):
        self.__brand = brand
        self.price = price

    def get_brand(self):
        return self.__brand

    def set_price(self, price: float):
        if price <= 5000:
            self.price = 10000.0
        else:
            self.price = price


class Car(Vehicle):

    def __init__(self):
        self.__brand = 'Brand'
        super().__init__(self.__brand, 2025)

    def get_brand(self):
        print(self.__brand)


vehicle = Vehicle("Tesla", 15200)
print(vehicle.year)
print(Vehicle.year)
print(Vehicle.AWS_USERNAME)
print(vehicle.get_brand())
print(vehicle.price)
vehicle.get_brand()
vehicle.set_price(-5)
print(vehicle.price)

car = Car()

car.get_brand()
