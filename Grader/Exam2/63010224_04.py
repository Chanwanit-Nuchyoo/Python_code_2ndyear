class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data

            if next is None:
                self.next = None
            else:
                self.next = next

        def __str__(self):
            return str(self.data)

    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self):
        if self.size > 0:
            p = self.head
            s = str(p.data)
            i = 1
            while i != self.size:
                p = p.next
                s += " <- " + str(p.data)
                i += 1
            return s
        else:
            return "Empty Queue"

    def __len__(self):
        return self.size

    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail = p
        self.size += 1

    def removeHead(self):
        if self.head == None: return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self):
        return self.size == 0

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.next
        return p

    def reorder(self):
        foundZero = False
        q1 = []
        q2 = []
        i = 1
        t = self.head
        if t.data != '0':
            q2.append(t.data)
        else:
            q1.append(t.data)
            foundZero = True

        while i != self.size:
            t = t.next
            if not foundZero:
                if t.data != '0':
                    q2.append(t.data)
                else:
                    q1.append(t.data)
                    foundZero = True
            else:
                q1.append(t.data)
            i += 1
        self.head = None
        self.tail = None
        self.size = 0
        for i in range(len(q1)):
            self.append(q1.pop(0))
        for i in range(len(q2)):
            self.append(q2.pop(0))


print(" *** Re order ***")
inp = input("Enter Input : ").split(" ")
ll = LinkedList()
for i in inp:
    ll.append(i)
print("Before : {}".format(ll.__str__()))
ll.reorder()
print("After : {}".format(ll.__str__()))

