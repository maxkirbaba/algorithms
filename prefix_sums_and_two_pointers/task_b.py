n, k = map(int, input().split())

first = 0
cur = 0
ans = 0

seq = list(map(int, input().split()))

for last in range(n):
    cur += seq[last]
    while first <= last and cur > k:
        cur -= seq[first]
        first += 1

    if cur == k:
        ans += 1

print(ans)
