tree = [None, None, None, 0]


def add_node(tree, value):
    if tree[0] is None:
        tree[0] = value

    elif value < tree[0]:
        if tree[1] is None:
            tree[1] = [value, None, None, 0]
        else:
            add_node(tree[1], value)
    elif value > tree[0]:
        if tree[2] is None:
            tree[2] = [value, None, None, 0]
        else:
            add_node(tree[2], value)

    height_left_child = tree[1][3] if tree[1] else -1
    height_right_child = tree[2][3] if tree[2] else -1
    tree[3] = max(height_left_child, height_right_child) + 1


def avl(tree):
    if tree is None:
        return True

    left_child = tree[1][3] if tree[1] else -1
    right_child = tree[2][3] if tree[2] else -1
    ans = abs(left_child - right_child) < 2
    return ans and avl(tree[1]) and avl(tree[2])


for i in map(int, input().split()):
    if i != 0:
        add_node(tree, i)

print("YES" if avl(tree) else "NO")
