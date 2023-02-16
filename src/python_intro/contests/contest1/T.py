i = int(input())
k = int(input())

if k <= i:
	print(1)
else:
	m = k % i
	if m % i != 0:
		print((k // i) + 1)
	else:
		print(k // i)