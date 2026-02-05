n = int(input())
seq = list(map(int, input().split()))


def symmetry(s):
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            if i == 0:
                return 0
            else:
                ans = s[:i][::-1]
                return f"{len(ans)}\n{" ".join(map(str, ans))}"


print(symmetry(seq))
