blocks = {}
for i in range(int(input())):
    key, value = input().split()
    blocks[key] = max(blocks.get(key, int(value)), int(value))

print(sum(blocks.values()))
