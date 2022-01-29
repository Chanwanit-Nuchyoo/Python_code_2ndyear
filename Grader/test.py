class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.size += 1

    def __str__(self):
        if self.size == 0:
            return "Empty"
        else:
            i = 2
            t = self.head
            r = "" + str(t.data)
            while i <= self.size:
                t = t.next
                r += " --> " + str(t.data)
                i += 1
        return r

    def pop(self):
        if self.size == 0:
            return "This list is empty"
        elif self.size == 1:
            t = self.tail.data
            self.head = None
            self.tail = None
            self.size -= 1
            return t
        else:
            t = self.tail
            pre = t.previous
            pre.next = None
            t.previous = None
            self.tail = pre
            self.size -= 1
            return t.data

    def pop_head(self):
        if self.size == 0:
            return "This list is empty"
        elif self.size == 1:
            t = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return t
        else:
            t = self.head
            next = t.next
            t.next = None
            next.previous = None
            self.head = next
            self.size -= 1
            return t.data

    def add_head(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def insert(self, index, data):
        if index >= 0:
            if index + 1 > self.size:
                print("index out of range")
            elif index == 0:
                self.add_head(data)
            else:
                i = 0
                new_node = Node(data)
                t = self.head
                while i != index:
                    t = t.next
                    i += 1
                pre = t.previous
                pre.next = new_node
                t.previous = new_node
                new_node.previous = pre
                new_node.next = t
                self.size += 1
        else:
            if abs(index) > self.size:
                print("index out of range")
            elif abs(index) == self.size:
                self.add_head(data)
            else:
                t = self.tail
                i = -1
                new_node = Node(data)
                while i != index:
                    t = t.previous
                    i -= 1
                pre = t.previous
                pre.next = new_node
                t.previous = new_node
                new_node.previous = pre
                new_node.next = t
                self.size += 1

    def remove(self, index):
        if index >= 0:
            if index + 1 > self.size:
                print("Index out of range.")
            elif index == 0:
                self.pop_head()
            elif index + 1 == self.size:
                self.pop()
            else:
                i = 0
                t = self.head
                while i != index:
                    t = t.next
                    i += 1
                pre = t.previous
                next = t.next
                pre.next = next
                next.previous = pre
                t.next = None
                t.previous = None
                self.size -= 1
        else:
            if abs(index) > self.size:
                print("index out of range")
            elif abs(index) == self.size:
                self.pop_head()
            elif index == -1:
                self.pop()
            else:
                i = -1
                t = self.tail
                while i != index:
                    t = t.previous
                    i -= 1
                pre = t.previous
                next = t.next
                pre.next = next
                next.previous = pre
                t.next = None
                t.previous = None
                self.size -= 1

list = List()
list.append(4)
print(list)
list.append(3)
print(list)
list.append(2)
print(list)
list.append(1)
print(list)


