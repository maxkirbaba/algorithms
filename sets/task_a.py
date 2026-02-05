def numberofdefnumbers(s):
    return len(set(s))


s = list(map(int, input().split()))
print(numberofdefnumbers(s))