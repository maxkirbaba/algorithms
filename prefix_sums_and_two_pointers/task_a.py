number_of_shirts = int(input())
colors_shirts = list(map(int, input().split()))
number_of_pants = int(input())
colors_pants = list(map(int, input().split()))

min_diff = 10**7
ans = ()
first1 = first2 = 0

while first1 < number_of_shirts and first2 < number_of_pants:
    diff = abs(colors_shirts[first1] - colors_pants[first2])
    if diff < min_diff:
        min_diff = diff
        ans = (colors_shirts[first1], colors_pants[first2])

    if colors_shirts[first1] < colors_pants[first2]:
        first1 += 1
    else:
        first2 += 1

    if min_diff == 0:
        break

print(" ".join(map(str, ans)))
