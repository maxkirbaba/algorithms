a = input()

ans = dict()
try:
    for i in a:
        ans[i] = ans.get(i, 0) + 1

    print(max(ans, key=ans.get))
except Exception:
    print(None)