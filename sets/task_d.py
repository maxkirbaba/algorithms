from sys import stdin

ans = set()
for i in stdin:
    for j in i.split():
        ans.add(j)

print(len(ans))