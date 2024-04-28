class Car:
    # Class variable
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # Increment total_cars each time a new instance is created
        Car.total_cars += 1

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Creating instances of Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Focus")

# Accessing class variable using class name
print("Total number of cars:", Car.total_cars)

# Accessing class variable using instance
print("Total number of cars:", car1.total_cars)

# Modifying class variable
Car.total_cars = 10
print("Total number of cars:", car2.total_cars)
