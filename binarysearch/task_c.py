width, height, n = map(int, input().split())

l = 1
r = max(width, height) * n
while l < r:
    m = (l + r) // 2
    if (m // width) * (m // height) >= n:
        r = m
    else:
        l = m + 1

print(l)
