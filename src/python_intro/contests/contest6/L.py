def reverse_number(n):
    reversed_number = 0

    while n > 0:
        current_digit = n % 10
        reversed_number = 10 * reversed_number + current_digit
        n //= 10

    return reversed_number

def is_palindrome(number_to_check):
    reversed_number = reverse_number(number_to_check)
    return reversed_number == number_to_check

a = int(input())
b = int(input())
for i in range(a, b + 1):
    if is_palindrome(i):
        print(i)