user_input = input("Enter a value: ")
if user_input.isdigit():
    number = int(user_input)
    print(f"The data type of the entered number is: {type(number)}")
else:
    try:
        number = float(user_input)
        print(f"The data type of the entered number is: {type(number)}")
    except ValueError:
              print(f"The data type of the entered value is: {type(user_input)}")
