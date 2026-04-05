tree = [None, None, None]


def add_node(tree, value, curr_depth=1):
    if tree[0] is None:
        tree[0] = value
        print(curr_depth, end=" ")

    elif value < tree[0]:
        if tree[1] is None:
            tree[1] = [value, None, None]
            print(curr_depth + 1, end=" ")
        else:
            add_node(tree[1], value, curr_depth + 1)

    elif value > tree[0]:
        if tree[2] is None:
            tree[2] = [value, None, None]
            print(curr_depth + 1, end=" ")
        else:
            add_node(tree[2], value, curr_depth + 1)


for i in map(int, input().split()):
    if i != 0:
        add_node(tree, i)
