def intersection(a, b):
    return " ".join(map(str, sorted(set(a) & set(b))))


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(intersection(a, b))