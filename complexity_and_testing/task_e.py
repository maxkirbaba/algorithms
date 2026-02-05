import math


app1, all_floors, app2, p2, floor2 = list(map(int, input().split()))

all_options = []

for x in range(1, 1001):
    app_in_p = all_floors * x

    p = math.ceil(app2 / app_in_p)
    floor = math.ceil((app2 - ((p - 1) * app_in_p)) / x)

    if p == p2 and floor == floor2:
        p1 = math.ceil(app1 / app_in_p)
        floor1 = math.ceil((app1 - ((p1 - 1) * app_in_p)) / x)
        all_options.append((p1, floor1))

if not all_options:
    print(-1, -1)

else:
    p_values = {p for p, f in all_options}
    f_values = {f for p, f in all_options}

    p_ans = all_options[0][0] if len(p_values) == 1 else 0
    f_ans = all_options[0][1] if len(f_values) == 1 else 0

    print(p_ans, f_ans)
