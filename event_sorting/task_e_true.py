res = 0
n = int(input())
a = [0] * 1440
for i in range(n):
    h1, m1, h2, m2 = map(int, input().split())
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    if t1 >= t2:
        for j in range(t1, 1440):
            a[j] += 1
        for j in range(t2):
            a[j] += 1
    else:
        for j in range(t1, t2):
            a[j] += 1
for i in a:
    if i == n:
        res += 1
print(res)
