class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next


class Linkedlist:

    def __init__(self):
        self.head = None

    def append(self,item):
        data = Node(item)
        if self.head is None:
            self.head = data
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = data

    def __str__(self):
        t = self.head
        r = "" + t.data
        while t.next is not None:
            t = t.next
            r = r + " <- " + str(t.data)
        return r

    def pop_head(self):
        t = self.head
        next = t.next
        self.head = next
        return t.data

    def size(self):
        t = self.head
        i = 0
        while t.next is not None:
            t = t.next
            i = i+1
        return i

    def pop(self):
        t = self.head
        pre = None
        while t.next is not None:
            pre = t
            t = t.next
        pre.next = None
        return t

    def locomotive(self):
        t = self.head
        while t.data != '0':
            t = t.next
            temp = self.pop_head()
            self.append(temp)
        return self


print(" *** Locomotive ***")
inp = input("Enter Input : ").split()
LKL = Linkedlist()
for item in inp:
    LKL.append(item)
print("Before : {}".format(LKL))
print("After : {}".format(LKL.locomotive()))

