count_segments, count_points = map(int, input().split())

events = []
for _ in range(count_segments):
    start, finish = map(int, input().split())
    # if start > finish:
    #     start, finish = finish, start
    events.append((start, -1))
    events.append((finish, 1))

points = list(map(int, input().split()))
for i, point in enumerate(points):
    events.append((point, 0, i))

events.sort()

cur = 0
ans = [0] * count_points

for event in events:
    if event[1] == 0:
        ans[event[2]] = cur
    elif event[1] == -1:
        cur += 1
    elif event[1] == 1:
        cur -= 1

print(" ".join(map(str, ans)))
