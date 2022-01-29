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
            s = 'Linked data : '
            p = self.head
            while p != None:
                s += str(p.data) + ' '
                p = p.next
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

    def reverse(self):
        list = []
        i = 0
        t = self.head
        while i != self.size:
            list.append(t.data)
            t = t.next
            i += 1
        self.head = None
        self.tail = None
        for i in range(len(list)):
            self.append(list.pop())


numbers = [str(x) for x in input("Enter numbers : ").split(" ")]
ll = LinkedList()
for i in numbers:
    ll.append(i)
print("Linkedlist Before Reverse")
print(ll)
print("Linkedlist After Reverse")
ll.reverse()
print(ll)