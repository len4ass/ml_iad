a = int(input())
b = int(input())
c = int(input())

def oddeven(x):
	odd = 0
	even = 0

	if x % 2 == 0:
		even += 1
	else:
		odd += 1

	return odd, even

ao, ae = oddeven(a)
bo, be = oddeven(b)
co, ce = oddeven(c)

r = ao + bo + co
s = ae + be + ce

if r >= 1 and s >= 1:
	print("YES")
else:
	print("NO")