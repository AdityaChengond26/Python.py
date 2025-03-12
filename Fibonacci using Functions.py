def fib(n):
  a=0
  b=1
  if n==1:
    print("0")
  else:
      print(a)
      print(b)
  for i in range(2,n):
     a,b=b,a+b
     print(b)
