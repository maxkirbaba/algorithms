n = int(input())
keys = list(map(int, input().split()))
k = int(input())
seq = list(map(int, input().split()))
for i in seq:
    keys[i - 1] -= 1

for j in keys:
    if j < 0:
        print("YES")
    else:
        print("NO")
