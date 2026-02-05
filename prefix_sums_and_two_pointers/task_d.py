n, r = map(int, input().split())
monuments = list(map(int, input().split()))

ans = 0
right = 0
for left in range(len(monuments)):
    while right < len(monuments) and monuments[right] - monuments[left] <= r:
        right += 1
    ans += len(monuments) - right

print(ans)
