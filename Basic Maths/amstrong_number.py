def amstrong(num):

    sum = 0
    temp = num
    while temp > 0:
        last_digit = temp % 10
        sum += last_digit ** 3
        temp //= 10

    return sum == num

num = int(input("Enter a number: "))

if amstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")