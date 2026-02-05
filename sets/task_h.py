n = int(input())

ans = set()
for i in range(n):
    x, y = map(int, input().split())
    ans.add(x)

print(len(ans))