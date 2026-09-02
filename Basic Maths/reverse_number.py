def reverse(num):
    rev = 0
    while num > 0:
        last_digit = num % 10
        rev = rev * 10 + last_digit
        num = num // 10
    return rev

def reverse_recursive(num, rev = 0):
    if num ==0:
        return rev

    return reverse_recursive(num // 10, rev * 10 + num % 10)

num = int(input("Enter a number: "))

print(f"The reverse of {num} is: {reverse(num)}")
print(f"The reverse of {num} using recursion is: {reverse_recursive(num)}")

