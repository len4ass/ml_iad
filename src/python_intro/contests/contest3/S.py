a = int(input())

reversed_number = 0

while a > 0:
    current_digit = a % 10
    reversed_number = 10 * reversed_number + current_digit
    a //= 10

print(reversed_number)

