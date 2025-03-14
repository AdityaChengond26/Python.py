class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def data(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def data(self):
        super().data()
        print(f"Seats: {self.seats}")

car = Car("Toyota", "Corolla", 5)
car.data()

