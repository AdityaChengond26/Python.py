# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Iu2dUorxli0RnMGXYfUeFSkSlzn8VWjd
"""

def sum_of_squares(n):
    total = 0
    for i in range(1, n+1):
        total += i**2
    return total

n = int(input("Enter a number: "))
print("Sum of squares:", sum_of_squares(n))

