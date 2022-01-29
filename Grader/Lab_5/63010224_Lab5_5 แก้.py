class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class LinkedList(object):

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d)
        if self.root is None:
            self.root = new_node
            self.size += 1
        else:
            h = self.root
            if h.get_next() is None:
                h.set_next(new_node)
                self.size += 1
            else:
                while h.get_next() is not None:
                    h = h.get_next()
                h.set_next(new_node)
                self.size += 1

    def add_head(self, n):
        new_node = Node(n, self.root)
        self.root = new_node
        self.size += 1

    def pop_head(self):
        p = self.root.data
        if self.root.get_next() is not None:
            self.root = self.root.get_next()
            self.size -= 1
        else:
            self.root = None
            self.size = 0
        return p

    def __str__(self):
        r = self.root
        if r is not None:
            m = str(r.get_data())
            while r.get_next() is not None:
                r = r.get_next()
                m = m + " -> " + str(r.get_data())
            return m
        else:
            return ""


def get_max_bits(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i


def get_digit(n, d):
    t = abs(n)
    for i in range(d - 1):
        t //= 10
    return t % 10


def sortList(H):
    head = H
    current = H
    index = None

    if (H == None):
        return
    else:
        while (current != None):
            index = current.get_next()

            while (index != None):
                if (current.data < index.data):
                    temp = current.data
                    current.data = index.data
                    index.data = temp
                index = index.get_next()
            current = current.get_next()
        return head


def radix_sort(l=[]):
    q = LinkedList()
    b = LinkedList()
    for i in l:
        q.add(i)
        b.add(i)
    qq = [LinkedList(), LinkedList(), LinkedList(), LinkedList(), LinkedList(), LinkedList(), LinkedList(),
          LinkedList(), LinkedList(), LinkedList()]
    digit = 1
    continue_ = True
    while continue_:
        while q.get_size() != 0:
            num = q.pop_head()
            num_digit = get_digit(num, digit)
            qq[num_digit].add(num)
            for y in range(10):
                qq[y].root = sortList(qq[y].root)
            if qq[0].size == len(l):
                continue_ = False
        print("------------------------------------------------------------")
        print("Round : {}".format(digit))
        for x in range(10):
            print("{} : {}".format(x, str(qq[x]).replace("-> ", "")))
        for i in range(10):
            while qq[i].get_size() != 0:
                q.add(qq[i].pop_head())
            q.root = sortList(q.root)
        digit += 1
    return q, b, digit - 2


inp = [int(x) for x in input("Enter Input : ").split()]
sorted_list, before, round = radix_sort(inp)
print("------------------------------------------------------------")
print("{} Time(s)".format(round))
print("Before Radix Sort : {}".format(before))
print("After  Radix Sort : {}".format(sorted_list))
