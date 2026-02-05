a = list(map(int, input().split()))


def grow(a):
    for i in range(1, len(a)):
        if a[i] <= a[i - 1]:
            return "NO"
    return "YES"


print(grow(a))
