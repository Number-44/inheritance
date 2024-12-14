class Car:
    def __init__(self, name, brand):
        self.model_name = name
        self.model_brand = brand

    def launch(self):
        print(f"{self.model_name} by {self.model_brand} launched!")


# Creating an object of the Car class
car1 = Car("Ghost", "Rolls-Royce")
car1.launch()

# Class Benz inherits the launch method from Car
class Benz(Car):
    pass


# Creating an object of the Benz class
h1 = Benz("McLaren", "Benz")
h1.launch()
