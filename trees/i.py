import sys

sys.setrecursionlimit(100000)


def count_descendants(name, tree, cache):
    if name in cache:
        return cache[name]

    count = 0
    if name in tree:
        for child in tree[name]:
            count += 1 + count_descendants(child, tree, cache)

    cache[name] = count
    return count


tree = {}
all_names = set()
for _ in range(int(input()) - 1):
    child, parent = input().split()
    if parent not in tree:
        tree[parent] = []

    tree[parent].append(child)
    all_names.add(child)
    all_names.add(parent)

cache = {}
for name in sorted(all_names):
    print(f"{name} {count_descendants(name, tree, cache)}")
