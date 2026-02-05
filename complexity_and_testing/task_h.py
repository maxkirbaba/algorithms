a, b, n, m = [int(input()) for i in range(4)]
min_1 = a * (n - 1) + n
max_1 = a * (n + 1) + n
min_2 = b * (m - 1) + m
max_2 = b * (m + 1) + m

if min_1 > max_2 or min_2 > max_1:
    print(-1)
else: 
    print(max(min_1, min_2), min(max_1, max_2))