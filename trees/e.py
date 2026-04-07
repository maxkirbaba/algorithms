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


def leaf_output(tree):
    if tree[1] is None and tree[2] is None:
        print(tree[0])
    if tree[1]:
        leaf_output(tree[1])
    if tree[2]:
        leaf_output(tree[2])


for i in map(int, input().split()):
    if i != 0:
        add_node(tree, i)

leaf_output(tree)
