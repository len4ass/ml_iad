a = int(input())
b = int(input())
c = int(input())

co = 0
if a == b == c:
	co = 3
elif (a == b) or (b == c) or (a == c):
	co = 2
else:
	co = 0

print(co)