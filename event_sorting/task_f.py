n = int(input())

events = []
for i in range(1, n + 1):
    d_b, m_b, y_b, d_d, m_d, y_d = map(int, input().split())

    date_18 = (y_b + 18, m_b, d_b)
    death = (y_d, m_d, d_d)
    date_80 = (y_b + 80, m_b, d_b)

    endl = min(death, date_80)

    if date_18 < endl:
        events.append((date_18, 1, i))
        events.append((endl, -1, i))

events.sort()

ans = []
curr_p = set()
prev_date = None

for date, typ, n in events:
    if prev_date is not None and date != prev_date:
        if curr_p:
            ans.append(tuple(sorted(curr_p)))

    if typ == 1:
        curr_p.add(n)
    else:
        curr_p.remove(n)

    prev_date = date

if curr_p:
    ans.append(tuple(sorted(curr_p)))

ans = list(set(ans))

ans.sort(key=lambda x: -len(x))


def is_subset(a, b):
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            return False
    return i == len(a)


anss = []
for s in ans:
    if not any(is_subset(s, t) for t in anss):
        anss.append(s)

if not anss:
    print(0)
else:
    for s in anss:
        print(*s)
