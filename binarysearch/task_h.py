n, k = map(int, input().split())
summ = 0
nums = []
for _ in range(n):
    num = int(input())
    summ += num
    nums.append(num)

r = summ // k
l = 0

while l < r:
    m = (l + r + 1) // 2
    s = 0
    for i in nums:
        s += i // m
    if s >= k:
        l = m
    else:
        r = m - 1

print(r)
