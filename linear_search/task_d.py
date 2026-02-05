seq = list(map(int, input().split()))


def rock(s):
    cnt = 0
    for i in range(1, len(s) - 1):
        if s[i - 1] < s[i] > s[i + 1]:
            cnt += 1
    return cnt


print(rock(seq))
