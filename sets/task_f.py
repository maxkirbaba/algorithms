a = dict()
first_genom = input()
for i in range(1, len(first_genom)):
    a[first_genom[i - 1] + first_genom[i]] = a.get(first_genom[i - 1] + first_genom[i], 0) + 1

b = set()
second_genom = input()
for j in range(1, len(second_genom)):
    b.add(second_genom[j - 1] + second_genom[j])

ans = 0
for m in b:
    if m in a:
        ans += a[m]
print(a, b, ans)

