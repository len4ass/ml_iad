secs = int(input())
mins = 0
while secs >= 60:
	mins += 1
	secs -= 60

hrs = 0
while mins >= 60:
	hrs += 1
	mins -= 60

hrs %= 24
print(f"{hrs}:{mins:02d}:{secs:02d}")