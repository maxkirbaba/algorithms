n, m = map(int, input().split())

events = []
for _ in range(m):
    firstp, lastp = map(int, input().split())
    events.append((firstp, 1))
    events.append((lastp + 1, -1))

events.sort()
print(events)
prev = 0
free = 0
under_vision = 0

for pos, type in events:
    if pos > n:
        pos = n

    if under_vision == 0:
        free += pos - prev

    under_vision += type
    prev = pos

if prev < n and under_vision == 0:
    free += n - prev

print(free)
