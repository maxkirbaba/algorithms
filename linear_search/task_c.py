n = int(input())
seq = list(map(int, input().split()))
x = int(input())

a = float("inf")
ans = 0
for i in seq:
    if abs(x - i) < a:
        a = abs(x - i)
        ans = i

print(ans)