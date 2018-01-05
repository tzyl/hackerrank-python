class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        y = None
        z = self.root
        while z is not None:
            y = z
            if x.key < z.key:
                z = z.left
            else:
                z = z.right
        x.parent = y
        if y is None:
            self.root = x
        elif x.key < y.key:
            y.left = x
        else:
            y.right = x

    def successor(self, x):
        if x.right is not None:
            return self.minimum(x.right)
        y = x.parent
        while y is not None and x is not y.left:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if x.left is not None:
            return self.maximum(x.left)
        y = x.parent
        while y is not None and x is not y.right:
            x = y
            y = y.parent
        return y

    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def maximum(self, x):
        while x.right is not None:
            x = x.right
        return x


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


n = int(input())
A = [int(s) for s in input().strip().split()]

minimum_loss = float("inf")
bst = BinarySearchTree()
for price in A:
    x = Node(price)
    bst.insert(x)
    y = bst.successor(x)
    if y is not None:
        minimum_loss = min(minimum_loss, y.key - x.key)
print(minimum_loss)
