height = int(input())
lenght = int(input())
tiles = int(input())

r = min(height, lenght) // 2
l = 0

while l < r:
    k = (l + r + 1) // 2
    if lenght * height - (lenght - 2 * k) * (height - 2 * k) <= tiles:
        l = k
    else:
        r = k - 1

print(r)
