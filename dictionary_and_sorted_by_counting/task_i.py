dictionary = dict()
for _ in range(int(input())):
    s = input()
    slower = s.lower()
    if slower not in dictionary:
        dictionary[slower] = set()
    dictionary[slower].add(s)
    

print(dictionary)
ans = 0
for word in input().split():
    lword = word.lower()
    if lword in dictionary:
        if word not in dictionary[lword]:
            ans += 1
        
    else:
        upsymbol = 0
        for symbol in word:    
            if symbol.isupper():
                upsymbol += 1
        if upsymbol != 1:
            ans += 1
print(ans)
    