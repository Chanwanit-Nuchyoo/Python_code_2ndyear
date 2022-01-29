class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
            return

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def preorder(self):
        print(str(self.data) + " ", end="")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(str(self.data) + " ", end="")
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(str(self.data) + " ", end="")

    def bfs(self, root):
        if root is None:
            return
        Q = []
        Q.append(root)
        while len(Q) != 0:
            node = Q.pop(0)
            if node is None:
                continue
            print(node.data, end=" ")
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)


inp = [int(x) for x in input("Enter Input : ").split(" ")]
T = Node()
for i in inp:
    T.insert(i)
print("Preorder : ", end="")
T.preorder()
print("")
print("Inorder : ", end="")
T.inorder()
print("")
print("Postorder : ", end="")
T.postorder()
print("")
print("Breadth : ", end="")
T.bfs(T)
