# memory initialization
def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i + 1, 0])  # add in memory [key, left son, right son]
    return [memory, 0]  # [memory, first free element]


# fill the memory cell
def newnode(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]  # add new first free element
    return firstfree


# frees a cell
def delnode(memstruct, index):
    memory, firstsree = memstruct
    memory[index][1] = firstsree
    memstruct[1] = index


# finding element in tree
def find(memstruct, root, x):
    key = memstruct[0][root][0]  # current element value
    if key == x:
        return root

    elif x < key:
        left = memstruct[0][root][1]
        if left == -1:  # if left element not found return -1
            return -1
        else:  # else run recursive function
            return find(memstruct, left, x)

    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            return -1
        else:
            return find(memstruct, right, x)

            # addition element to tree if it was not there


# function for create and fill new node
def createandfillnode(memstruct, key):
    index = newnode(memstruct)
    memstruct[0][index][0] = key  # in key cell add new key
    memstruct[0][index][1] = -1  # in left son cell add -1, because it not there
    memstruct[0][index][2] = -1  # in right son cell add -1, because it not there
    return index


def add(memstruct, root, x):
    key = memstruct[0][root][0]
    if x < key:
        left = memstruct[0][root][1]
        if left == -1:  # if left son == -1, it is place for create new node
            memstruct[0][root][1] = createandfillnode(memstruct, key)
        else:  # else continue to look for a place
            add(memstruct, left, x)

    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            memstruct[0][root][2] = createandfillnode(memstruct, key)
        else:
            add(memstruct, right, x)


b = initmemory(20)
root = createandfillnode(b, 8)
print(b)
add(b, root, 10)
print(b)
add(b, root, 9)
print(b)
add(b, root, 14)
print(b)
add(b, root, 13)
print(b)
add(b, root, 3)
print(b)
