n = int(input())

events = []
for i in range(n):
    timing = list(map(int, input().split()))
    events.append((timing[0] * 60 + timing[1], 1, i + 1))
    events.append((timing[2] * 60 + timing[3], -1, i + 1))

events.sort()

open_cash_reg = set()
count_open_cr = 0
time_cr = 0
ans = 0

for t, i, pos in events:
    if i == 1:
        open_cash_reg.add(pos)
        count_open_cr += 1
        if count_open_cr == n:
            time_cr = t

    else:
        if pos in open_cash_reg:
            open_cash_reg.remove(pos)
            count_open_cr -= 1
            if count_open_cr == n - 1:
                ans += t - time_cr

if len(open_cash_reg) != 0:
    for t, i, pos in events:
        if i == 1:
            open_cash_reg.add(pos)
            count_open_cr += 1
            if count_open_cr == n:
                time_cr = t

        else:
            if pos in open_cash_reg:
                open_cash_reg.remove(pos)
                count_open_cr -= 1
                if count_open_cr == n - 1:
                    ans += t - time_cr
            print(ans)
            break

else:
    print(ans)
