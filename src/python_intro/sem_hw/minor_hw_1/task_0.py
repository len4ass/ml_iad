# Реверс числа
def reverse_number(n):
    reversed_number = 0

    while n > 0:
        current_digit = n % 10
        reversed_number = 10 * reversed_number + current_digit
        n //= 10

    return reversed_number

# Чекаем на палиндром
def is_palindrome(number_to_check):
    reversed_number = reverse_number(number_to_check)
    return reversed_number == number_to_check

if __name__ == '__main__':
    number = int(input())
    print(is_palindrome(number) and "palindrome" or "not palindrome")
