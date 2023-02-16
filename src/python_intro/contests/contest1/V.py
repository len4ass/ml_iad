i = int(input())
k = i % 100
i = i // 100
k = k // 10 + k % 10 * 10
print(i - k + 1)