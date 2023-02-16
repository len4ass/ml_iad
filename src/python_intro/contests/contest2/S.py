n = int(input())

if n % 10 == 1 and n != 11:
    print(f"{n} korova")
elif n % 10 >= 2 and n % 10 <= 4 and n // 10 != 1:
	print(f"{n} korovy")
else:
    print(f"{n} korov")