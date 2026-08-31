
def binaryTOdecimal(n):
    pow = 1
    ans = 0
    while n > 0:
        rem = n % 10
        ans += rem * pow 
        pow *= 2
        n = n // 10
    return ans 

def useRecursion(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + 2 * useRecursion(n // 10)

binary_number = int(input("enter a binary number: "))
decimal_number = binaryTOdecimal(binary_number)
print(f"The decimal representation of {binary_number} is: {decimal_number}")
recursive_decimal = useRecursion(binary_number)
print(f"The decimal representation of {binary_number} using recursion is: {recursive_decimal}")
