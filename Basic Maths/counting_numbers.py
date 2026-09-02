def count(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count 

n = int(input("Enter a number: "))
number_of_digits = count(n)
print(f"The number of digits in {n} is: {number_of_digits}")
