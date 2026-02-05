t_room, t_cond = list(map(int, input().split()))
mode = input()

if mode == "freeze":
    if t_room <= t_cond:
        print(t_room)
    else:
        print(t_cond)

if mode == "heat":
    if t_room >= t_cond:
        print(t_room)
    else:
        print(t_cond)

if mode == "auto":
    print(t_cond)

if mode == "fan":
    print(t_room)