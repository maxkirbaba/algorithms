tree = [None, None, None]


def add_node(tree, key):
    if tree[0] is None:
        tree[0] = key

    elif key < tree[0]:
        if tree[1] is None:
            tree[1] = [key, None, None]
        else:
            add_node(tree[1], key)

    elif key > tree[0]:
        if tree[2] is None:
            tree[2] = [key, None, None]
        else:
            add_node(tree[2], key)


def traverse_and_add_in_s(tree, s=None):
    if s is None:
        s = []
    if tree:
        traverse_and_add_in_s(tree[1], s)
        s.append(tree[0])
        traverse_and_add_in_s(tree[2], s)
    return s


for i in map(int, input().split()):
    if i != 0:
        add_node(tree, i)

print(traverse_and_add_in_s(tree)[-2])
