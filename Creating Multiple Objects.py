# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TD8wKmOWPm1VWOEgz0nkdh5qwxOWJPOR
"""

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

