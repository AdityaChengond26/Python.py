n = 10
try:
    result = n / 0

except ZeroDivisionError:
    print("Can't be divided by zero!")

try:
    n = 0
    res = 100 / n

except ZeroDivisionError:
    print("You can't divide by zero!")

finally:
    print("Execution complete.")

def divide(x, y):
  if y == 0:
    raise ZeroDivisionError("Cannot divide by zero!")
  return x / y
divide(10, 5)

