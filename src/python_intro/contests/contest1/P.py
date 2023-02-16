i = int(input())
k = 0
while i >= 60:
	k += 1
	i -= 60

k %= 24
print(f"{k} {i}")