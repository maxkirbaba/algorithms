n, x, y = map(int, input().split())

r = 10**9
l = 0

while l < r:
    m = (r + l) // 2
    if ((m // x) + (m // y)) >= n - 1:
        r = m
    else:
        l = m + 1
print(l + min(x, y))
