count_2 = int(input())
count_3 = int(input())
count_4 = int(input())

r = 10**15
l = 0

while l < r:
    m = (r + l) // 2
    if ((m * 5 + count_2 * 2 + count_3 * 3 + count_4 * 4) / (m + count_4 + count_2 + count_3)) >= 3.5:
        r = m
    else:
        l = m + 1

print(l)
