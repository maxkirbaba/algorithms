n, k = map(int, input().split())
numbers = list(map(int, input().split()))

count_nums = dict()
for i in numbers:
    count_nums[i] = count_nums.get(i, 0) + 1

uniqnums = list(count_nums.keys())
uniqnums.sort()

right = 0
duplicates = 0
ans = 0
for left in range(len(uniqnums)):
    while right < len(uniqnums) and uniqnums[left] * k >= uniqnums[right]:
        if count_nums[uniqnums[right]] >= 2:
            duplicates += 1
        right += 1

    rangelen = right - left
    if count_nums[uniqnums[left]] >= 2:
        ans += (rangelen - 1) * 3

    if count_nums[uniqnums[left]] >= 3:
        ans += 1

    ans += (rangelen - 1) * (rangelen - 2) * 3
    if count_nums[uniqnums[left]] >= 2:
        duplicates -= 1

    ans += duplicates * 3

print(ans)
