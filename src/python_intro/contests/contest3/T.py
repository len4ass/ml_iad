def reverse(a):
    reversed_number = 0

    while a > 0:
        current_digit = a % 10
        reversed_number = 10 * reversed_number + current_digit
        a //= 10

    return reversed_number

i = int(input())
c = 1
m = 0
while c <= i:
    r = reverse(c)
    if r == c:
        m += 1

    c += 1

print(m)