
def decimalTObinary(n):
    ans = 0 
    pow = 1
    while n > 0:
        rem = n % 2
        n = n // 2
        ans += rem * pow
        pow *= 10
    return ans

def usingRecursion(n):
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * usingRecursion(n // 2)

decimal_number = int(input("Enter a decimal number: "))
binary_number = decimalTObinary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_number}")

# Test the recursive function as well
recursive_binary = usingRecursion(decimal_number)
print(f"The binary representation of {decimal_number} using recursion is: {recursive_binary}")