n, m, k = map(int, input().split())


table = [[0 for _ in range(m)] for _ in range(n)]


mines = []
for _ in range(k):
    p, q = map(int, input().split())
    p -= 1
    q -= 1

    table[p][q] = "*"
    mines.append((p, q))


for i, j in mines:
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and table[ni][nj] != "*":
                table[ni][nj] += 1

for row in table:
    print(" ".join(str(s) for s in row))
