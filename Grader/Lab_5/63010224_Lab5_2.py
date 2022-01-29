class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        data = Node(item)
        if self.isEmpty():
            self.head = data
            self.tail = self.head
        else:
            pre = self.tail
            data.previous = pre
            pre.next = data
            self.tail = data

    def addHead(self, item):
        data = Node(item)
        if self.isEmpty():
            self.head = data
            self.tail = self.head
        else:
            next = self.head
            next.previous = data
            data.next = next
            self.head = data

    def insert(self, pos, item):
        if pos < 0:
            dest = abs(pos)
            index = 1
            self.tail
        if self.isEmpty():
            self.append(item)
        elif pos == 0:
            self.addHead(item)
        elif pos == -1:
            data = Node(item)
            t = self.tail
            pre = t.previous
            pre.next = data
            data.previous = pre
            data.next = t
            t.previous = data

        elif pos > int(self.size())-1 and pos >0:
            self.append(item)
        elif abs(pos) > int(self.size()) and pos <0:
            self.addHead(item)
        elif pos > 0:
            t = self.head
            index = 0
            while index != pos:
                t = t.next
                index= index+1
            data = Node(item)
            pre = t.previous
            pre.next = data
            data.previous = pre
            data.next = t
            t.previous = data
        elif pos < 0:
            t = self.tail
            index = 1
            while index != abs(pos):
                t = t.previous
                index = index + 1
            data = Node(item)
            pre = t.previous
            pre.next = data
            data.previous = pre
            data.next = t
            t.previous = data



    def search(self, item):
        t = self.head
        while t:
            if t.value != item:
                t = t.next
            else:
                return "Found"
        return "Not Found"

    def index(self, item):
        pos = 0
        t = self.head
        while t:
            if t.value != item:
                t = t.next
                pos = pos + 1
            else:
                return str(pos)
        return "-1"

    def size(self):
        if self.isEmpty():
            return "0"
        else:
            t = self.head
            size = 0
            while t:
                t = t.next
                size = size + 1
            size = str(size)
            return size

    def pop(self, pos):
        if abs(pos) > int(self.size())-1 and pos >=0:
            return "Out of Range"
        elif abs(pos) > int(self.size()) and pos < 0:
            return "Out of Range"
        elif pos < 0:
            t = self.tail
            while t is not None:
                alt_index = int(self.index(t.value)) - int(self.size())
                print(alt_index)
                if alt_index != pos:
                    t = t.previous
                else:
                    if t.next is None:
                        if t.previous is None:
                            self.head = None
                            self.tail = None
                        else:
                            pre = t.previous
                            pre.next = None
                            self.tail = pre
                    else:
                        if t.previous is None:
                            next = t.next
                            next.previous = None
                            self.head = next
                        else:
                            pre = t.previous
                            next = t.next
                            pre.next = next
                            next.previous = pre
                    return "Success"
                    break
        else:
            t = self.head
            while t is not None:
                index = int(self.index(t.value))
                if index != pos:
                    t = t.next
                else:
                    if t.previous is None:
                        if t.next is None:
                            self.head = None
                            self.tail = None
                        else:
                            next = t.next
                            next.previous = None
                            self.head = next
                    else:
                        if t.next is None:
                            pre = t.previous
                            pre.next = None
                            self.tail = pre
                        else:
                            pre = t.previous
                            next = t.next
                            pre.next = next
                            next.previous = pre
                    return "Success"
                    break

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {} : {}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())