# Creating tree node
class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


# created search binary tree
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        # Add new element to tree
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_recursive(self.root, key)

    # search free place for add new node
    def insert_recursive(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert_recursive(node.left, key)

        elif key > node.value:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert_recursive(node.right, key)

    # search element
    def search(self, key):
        return self.search_recursive(self.root, key)

    def search_recursive(self, node, key):
        if node is None:
            return False
        if node.value == key:
            return True
        elif key < node.value:
            return self.search_recursive(node.left, key)
        else:
            return self.search_recursive(node.right, key)

    # tree travelsal
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value)
            self._inorder(node.right)

    # tree depth
    def depth(self, node):
        if node is None:
            return 0

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        return max(left_depth, right_depth) + 1


tree = BinaryTree()
for i in list(map(int, input().split()))[:-1]:
    tree.insert(i)
    print(tree.depth())
