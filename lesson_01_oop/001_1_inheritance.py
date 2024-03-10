class Vehicle:
    # static members

    year = 2024
    AWS_USERNAME = "user"

    def __init__(self, brand: str, price: float = 350.56):
        self.__brand = brand
        self.price = price

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand


class Car(Vehicle):

    def __init__(self, brand: str, price: float, is_electrical: bool):
        super().__init__(brand, price)
        self.is_electrical = is_electrical

    def get_brand(self):
        print(self.__brand)


vehicle = Vehicle("Tesla", 15200)
print(vehicle.year)
print(Vehicle.year)
print(Vehicle.AWS_USERNAME)
print(vehicle.brand)
print(vehicle.price)

vehicle.brand = "GENERAL"
print(vehicle.price)

car = Car("General", 1000000, True)
print(car.brand)

print(car.brand)
car.brand = "Opel"
print(car.brand)
