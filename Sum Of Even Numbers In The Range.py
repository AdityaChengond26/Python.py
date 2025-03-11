def sum_of_even_numbers(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total_sum += num
    return total_sum
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
result = sum_of_even_numbers(start, end)
print(f"The sum of all even numbers in the range {start} to {end} is: {result}")
