# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Iu2dUorxli0RnMGXYfUeFSkSlzn8VWjd
"""

num=int(input("Enter an integer"))
reversed_num=0
while num!=0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num//=10
print(reversed_num)