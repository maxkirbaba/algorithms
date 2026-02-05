n = int(input())

usedbefore = set()
for i in range(n):
    a, b = map(int, input().split())
    if a + b == n - 1 and a >= 0 and b >= 0 and a not in usedbefore:
        usedbefore.add(a)
print(len(usedbefore))