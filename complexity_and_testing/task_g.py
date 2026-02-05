n, k, m = map(int, input().split())

ans = 0
if k < m:
    print(0)
else:
    while n >= k:
        total_k = n // k
        n = n % k
        ans += total_k * (k // m)
        n += total_k * (k % m)
    print(ans)
