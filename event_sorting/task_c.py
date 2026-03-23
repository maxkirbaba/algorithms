count_students, d = map(int, input().split())
students = list(map(int, input().split()))

events = []
for i, student in enumerate(students):
    events.append((student, i))

events.sort()

ans = [0] * count_students
max_ticket = 0
active = []
start_idx = 0

for x, idx in events:
    while start_idx < len(active) and x - active[start_idx][0] > d:
        start_idx += 1

    used = set()
    for coord, ticket in active[start_idx:]:
        used.add(ticket)

    ticket = 1
    while ticket in used:
        ticket += 1

    ans[idx] = ticket
    max_ticket = max(max_ticket, ticket)

    active.append((x, ticket))

print(max_ticket)
print(*ans)
