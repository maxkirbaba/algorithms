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


def one_child(tree):
    if (tree[1] and tree[2] is None) or (tree[1] is None and tree[2]):
        if tree[1]:
            one_child(tree[1])
            print(tree[0])
        if tree[2]:
            print(tree[0])
            one_child(tree[2])
    elif tree[1] and tree[2]:
        one_child(tree[1])
        one_child(tree[2])


for i in map(int, input().split()):
    if i != 0:
        add_node(tree, i)

one_child(tree)
