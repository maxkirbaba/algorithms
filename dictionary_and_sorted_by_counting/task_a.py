dictionary = dict()
for _ in range(int(input())):
    s = input().split()
    dictionary[s[0]] = s[1]

word = input()
for key, value in dictionary.items():
    if word == key:
        print(value)
    elif word == value:
        print(key)