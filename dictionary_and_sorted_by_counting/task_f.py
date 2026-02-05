from sys import stdin


names = {}
for line in stdin:
    name, product, number = line.split()
    if name not in names:
        names[name] = {}
    if product not in names[name]:
        names[name][product] = int(number)
    else:
        names[name][product] += int(number)
        
names = dict(sorted(names.items()))
for n in names:
    print(f"{n}:")
    s = dict(sorted(names[n].items()))
    for i in s:
        print(f"{i} {s[i]}")