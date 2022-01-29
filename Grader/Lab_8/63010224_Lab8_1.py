class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            print("*")
            self.data = data
            return

        if data < self.data:
            print("L", end="")
            if self.left:
                self.left.insert(data)
            else:
                print("*")
                self.left = Node(data)
        elif data >= self.data:
            print("R", end="")
            if self.right:
                self.right.insert(data)
            else:
                print("*")
                self.right = Node(data)


inp = [int(x) for x in input("Enter Input : ").split(" ")]
T = Node()
for i in inp:
    T.insert(i)