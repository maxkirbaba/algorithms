def check(m, chekparams):
    minbrigades, c, heights = chekparams
    brigades = 0
    i = 0
    while i < len(heights) - c + 1:
        if heights[i + c - 1] - heights[i] <= m:
            brigades += 1
            i += c
        else:
            i += 1
    return brigades >= minbrigades


n, num_of_b, ch_in_b = map(int, input().split())

heights = []
for _ in range(n):
    heights.append(int(input()))
heights.sort()

r = heights[-1] - heights[0]
l = 0

while l < r:
    m = (l + r) // 2
    if check(m, (num_of_b, ch_in_b, heights)):
        r = m
    else:
        l = m + 1

print(l)
