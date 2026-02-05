a, b, c = list(map(int, input().split()))

ans = set()
if a != 0:
    d = b ** 2 - 4 * a * c
    if d >= 0:
        ans.add(((-b) + d ** 0.5) / (2 * a))
        ans.add(((-b) - d ** 0.5) / (2 * a))
        print(sorted(ans))
    else:
        print("нет корней")

elif a == 0 and b != 0 and c != 0:
    ans.add((-c) / b)
    print(sorted(ans))
elif a == 0 and b != 0 and c == 0:
    ans.add(0)
    print(sorted(ans))
elif a == 0 and b == 0 and c != 0:
    print("нет корней")
elif a == 0 and b == 0 and c == 0:
    print("бесконечно много решений")

