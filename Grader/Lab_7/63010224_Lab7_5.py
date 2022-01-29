class Et:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


def inorder(t):
    if t:
        if t.left:
            print("(", end="")
        inorder(t.left)
        print(t.data, end="")
        inorder(t.right)
        if t.right:
            print(")", end="")


def preorder(t):
    if t:
        print(t.data, end="")
        if t.left:
            preorder(t.left)
        if t.right:
            preorder(t.right)


def constructTree(postfix):
    stack = []

    for char in postfix:
        if char not in "+-*/":
            t = Et(char)
            stack.append(t)
        else:
            t = Et(char)
            t1 = stack.pop()
            t2 = stack.pop()
            t.right = t1
            t.left = t2

            stack.append(t)

    t = stack.pop()

    return t


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


postfix = input("Enter Postfix : ")
r = constructTree(postfix)
print("Tree :")
printTree(r)
print("--------------------------------------------------")
print("Infix : ", end="")
inorder(r)
print("")
print("Prefix : ", end="")
preorder(r)
