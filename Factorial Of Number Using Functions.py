def factorial(n):
  if n < 0:
    return
  elif n == 0:
    return 1
  else:
    fact = 1
    for i in range(1, n + 1):
      fact *= i
    return fact
num = int(input("Enter a non-negative integer: "))
result = factorial(num)
print(f"The factorial of", num, "is", result)
