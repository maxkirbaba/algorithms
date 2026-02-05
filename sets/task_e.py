a = set(map(int, input().split()))

b = set(int(i) for i in input())

print(len(b - a))