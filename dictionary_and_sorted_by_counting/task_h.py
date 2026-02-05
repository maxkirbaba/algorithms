def makedict(s):
    w = dict()
    for symbol in s:
        w[symbol] = w.get(symbol, 0) + 1
    return w


def matchdict(dict1, dict2):
    count = 0
    for i in dict1:
        if i in dict2 and dict1[i] == dict2[i]:
            count += 1
    return count


def modify1(sdict, wdict, symb):
    ans = 0
    if symb in wdict and sdict[symb] == wdict[symb]:
        ans = -1
    sdict[symb] -= 1
    if symb in wdict and sdict[symb] == wdict[symb]:
        ans = 1
    return ans


def modify2(sdict, wdict, symb):
    ans = 0
    if symb not in sdict:
        sdict[symb] = 0
    if symb in wdict and sdict[symb] == wdict[symb]:
        ans = -1
    sdict[symb] += 1
    if symb in wdict and sdict[symb] == wdict[symb]:
        ans = 1
    return ans
    

lenW, lenS = map(int, input().split())
w = input()
s = input()

wdict = makedict(w)
sdict = makedict(s[:lenW])
matchingdicts = matchdict(sdict, wdict)
answer = 0
if matchingdicts == len(wdict):
    answer += 1
for i in range(lenW, lenS):
    matchingdicts += modify1(sdict, wdict, s[i - lenW])
    matchingdicts += modify2(sdict, wdict, s[i])
    if matchingdicts == len(wdict):
        answer += 1
print(answer)
    