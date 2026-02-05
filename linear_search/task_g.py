seq = list(map(int, input().split()))

max1 = max2 = -(10**9)
min1 = min2 = 10**9
for i in seq:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2:
        max2 = i

    if i < min1:
        min2 = min1
        min1 = i
    elif i < min2:
        min2 = i

if max1 * max2 >= min1 * min2:
    print(*sorted([max2, max1]))
else:
    print(*sorted([min1, min2]))
