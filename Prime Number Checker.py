a = int(input("Enter the number: "))

if a > 1:
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")
