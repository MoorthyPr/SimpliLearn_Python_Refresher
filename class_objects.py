class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# Create a car instance
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()   
print(my_car.brand)
print(my_car)
