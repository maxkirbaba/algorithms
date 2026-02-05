a, b, c, d, e = [int(input()) for i in range(5)]
brick = sorted([a, b, c])
hole = sorted([d, e])
if brick[0] <= hole[0] and brick[1] <= hole[1]:
    print("YES")
else:
    print("NO")