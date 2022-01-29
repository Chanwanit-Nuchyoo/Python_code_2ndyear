class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            space = '     ' * level
            node_data = node.__str__()
            print(space, node_data)
            self.printTree(node.left, level + 1)

    def printAgain(self, node, k, level=0):
        if node != None:
            self.printAgain(node.right, k, level + 1)
            if node.data > k:
                space = '     ' * level
                node_data = str(int(node.__str__()) * 3)
                print(space, node_data)
            else:
                space = '     ' * level
                node_data = node.__str__()
                print(space, node_data)
            self.printAgain(node.left, k, level + 1)


inp, k = [x for x in input("Enter Input : ").split("/")]
inp = [int(x) for x in inp.split(" ")]
T = BST()
for i in inp:
    T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
T.printAgain(T.root, int(k))
