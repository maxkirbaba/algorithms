tree = [None, None, None]


def add_node(tree, value):
    if tree[0] is None:
        tree[0] = value

    elif value < tree[0]:
        if tree[1] is None:
            tree[1] = [value, None, None]
        else:
            add_node(tree[1], value)

    elif value > tree[0]:
        if tree[2] is None:
            tree[2] = [value, None, None]
        else:
            add_node(tree[2], value)


def height(tree, curr_h=1):
    if tree is None:
        return curr_h - 1
    return max(height(tree[1], curr_h + 1), height(tree[2], curr_h + 1))


for i in map(int, input().split()):
    if i != 0:
        add_node(tree, i)

print(tree)
print(height(tree))
