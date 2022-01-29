class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data is None:
            self.data = data
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif data >= self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


def closest(inp, k):
    close = 1
    for x in inp:
        if abs(x - k) < abs(close - k):
            close = x
    return close


inp, k = input("Enter Input : ").split("/")
inp = [int(x) for x in inp.split(" ")]
T = Node()
for i in inp:
    T.insert(i)
    T.printTree(T)
    print("--------------------------------------------------")
print("Closest value of {} : ".format(k) + str(closest(inp, int(k))))
