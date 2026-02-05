heights = []
n = int(input())
for _ in range(n):
    heights.append(list(map(int, input().split()))[1])

left_to_right = [0] * (n)
right_to_left = [0] * n

for i in range(1, len(heights)):
    left_to_right[i] = left_to_right[i - 1]
    right_to_left[i] = right_to_left[i - 1]

    if heights[i] > heights[i - 1]:
        left_to_right[i] += (heights[i] - heights[i - 1])
    
    if heights[i] < heights[i - 1]:
        right_to_left[i] += (heights[i - 1] - heights[i])

ans = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < b:
        ans.append(left_to_right[b - 1] - left_to_right[a - 1])
    else:
        ans.append(right_to_left[a - 1] - right_to_left[b - 1])

for i in ans:
    print(i)