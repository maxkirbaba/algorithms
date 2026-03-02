n, k = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

for number in second:
    l = 0
    r = n - 1
    while l < r:
        m = (l + r) // 2
        if first[m] >= number:
            r = m
        else:
            l = m + 1
    if first[l] == number:
        print("YES")
    else:
        print("NO")
