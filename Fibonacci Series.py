# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Iu2dUorxli0RnMGXYfUeFSkSlzn8VWjd
"""

n=int(input("enter number of terms"))
a,b=0,1
for i in range(n):
  print(a,end=" ")
  a,b=b,a+b

