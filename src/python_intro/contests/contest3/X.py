import math
count = 0
sum_ = 0
square = 0
n = int(input())

while n != 0:
    square += n * n
    sum_ += n
    count += 1
    n = int(input())

mean = sum_ / count
standard_deviation = math.sqrt((square - 2 * mean * sum_ + count * mean * mean) / (count - 1))

print(standard_deviation)