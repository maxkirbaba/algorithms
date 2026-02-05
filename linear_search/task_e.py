n = int(input())
seq = list(map(int, input().split()))


def place_vasya(s):
    vasya = -1
    max_s = max(s)
    flag = False

    for i in range(1, len(s) - 1):
        if s[i - 1] == max_s:
            flag = True
        if s[i] % 10 == 5 and flag and s[i + 1] < s[i] and vasya < s[i]:
            vasya = s[i]
    
    if vasya != -1:
        ans = 1
        for j in s:
            if j > vasya:
                ans += 1
        return ans
    else:
        return 0
    

print(place_vasya(seq))