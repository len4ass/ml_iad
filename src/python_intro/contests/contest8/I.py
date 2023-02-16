size, user_count = map(int, input().split())
array_of_sizes = []
for i in range(0, user_count):
    array_of_sizes += [int(input())]

amount = sum(array_of_sizes)
array_of_sizes = sorted(array_of_sizes)
while amount > size and user_count != 0:
    amount -= array_of_sizes.pop()
    user_count -= 1

print(user_count)

