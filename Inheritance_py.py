# -*- coding: utf-8 -*-
"""Inheritance.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gaB5Zjt7cBnNdh0VAKuWtmRDgpduGb5Y
"""

class Animal:
  def speak(self):
    print("I am an Animal")
class Dog(Animal):
  def speak(self):
     print("I Bark")
dog = Dog()
dog.speak()

