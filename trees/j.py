import sys

sys.setrecursionlimit(100000)


def get_height(name, parent_of, heights):
    if name in heights:
        return heights[name]

    if name not in parent_of:
        heights[name] = 0
        return 0

    parent = parent_of[name]
    heights[name] = get_height(parent, parent_of, heights) + 1
    return heights[name]


parent_of = {}
all_names = set()
for _ in range(int(input()) - 1):
    child, parent = input().split()
    parent_of[child] = parent
    all_names.add(child)
    all_names.add(parent)

heights = {}
for name in sorted(all_names):
    print(f"{name} {get_height(name, parent_of, heights)}")
