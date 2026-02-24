size_m = int(input())
operations = input()

prevlen = 0
ans = 0

for i in range(size_m, len(operations)):
    if operations[i] == operations[i - size_m]:
        prevlen += 1
        ans += prevlen
    else:
        prevlen = 0
print(ans)
