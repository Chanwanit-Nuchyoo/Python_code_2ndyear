class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right= None

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

def insert(root, newValue):
    if root is None:
        root = Node(newValue)
        return root
    if newValue < root.data:
        root.left= insert(root.left, newValue)
    else:
        root.right = insert(root.right, newValue)
    return root


def height(root):
    if root == None:
        return 0
    hleft = height(root.leftChild)
    hright = height(root.rightChild)
    if hleft > hright:
        return hleft + 1
    else:
        return hright + 1


print(" *** Binary Search Tree ***")
inp = input("Enter Input : ").split(" ")
print("")
T = Node(int(inp.pop(0)))
for i in inp:
    insert(T,int(i))
print(" --- Tree traversal ---")
print("Level order : ", end="")
T.bfs(T)
print("")
print("Preorder : ", end="")
T.preorder()
print("")
print("Inorder : ", end="")
T.inorder()
print("")
print("Postorder : ", end="")
T.postorder()
