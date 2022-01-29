class node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

    def set_next(self,next):
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self,item):
        data = node(item)
        if self.head is None:
            self.head = data
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = data

    def __str__(self):
        if self.head is not None:
            t = self.head
            r = "" + t.data
            while t.next is not None:
                t = t.next
                r = r + "->" + str(t.data)
            return r
        else:
            return "Empty"

    def size(self):
        if self.head is None:
            return 0
        else:
            t = self.head
            size = 1
            while t.next is not None:
                t = t.next
                size = size + 1
            return size

    def sn(self, index1, index2):
        if self.size() == 0:
            print("Error! {list is empty}")
        elif index1 > self.size()-1:
            print("Error! {index not in length}:" + " {}".format(index1))
        elif index2 > self.size()-1:
            self.append(index2)
            print("index not in length, append : {}".format(index2))
        else:
            n_1 = None
            n_2 = None
            t = self.head
            i = 0
            while t.next is not None:
                if i == index1:
                    n_1 = t
                if i == index2:
                    n_2 = t
                t = t.next
                i = i + 1
                if i == index1:
                    n_1 = t
                if i == index2:
                    n_2 = t
            n_1.set_next(n_2)
            print("Set node.next complete!, index:value = {1}:{0} -> {3}:{2}".format(n_1.data,index1,n_2.data,index2))

    def checkloop(self):
        t = self.head
        timeout = 20
        i = 1
        if self.head is not None:
            while t.next is not None:
                t = t.next
                if t is self.head:
                    return "Found Loop"
                i = i+1
                if i == timeout:
                    return "Found Loop"
        return "No Loop"


inp = input("Enter input : ").replace(","," ").replace(":"," ").split()


il = [x for x in inp if x not in "AS:,"]
cl = [y for y in inp if not y.isnumeric()]
lk = linkedlist()
for c in cl:
    if c == "A":
        lk.append(il.pop(0))
        print(lk)
    elif c == "S":
        index1 = int(il.pop(0))
        index2 = int(il.pop(0))
        lk.sn(index1,index2)

ack = lk.checkloop()
if ack == "No Loop":
    print(ack)
    print(lk)
else:
    print(ack)