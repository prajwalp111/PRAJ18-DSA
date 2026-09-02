from reverse_number import reverse

def palindrome(num):
    original_num = num
    rev_num = 0

    rev_num = reverse(original_num)
    
    return original_num == rev_num

num = int(input("Enter a number: "))

if palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")



def palindrome_string(str):
    return str[::-1]

str = input("Enter a string: ")

if str == palindrome_string(str):
    print(f"{str} is a palindrome.")
else:
    print(f"{str} is not a palindrome.")
