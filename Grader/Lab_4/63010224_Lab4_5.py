class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,i):
        self.items.append(i)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

class Stack():

    def __init__(self, *ls):
        self.items = [x for x in ls]

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


f = input("Enter Input (Normal, Mirror) : ").split()

mirror = "".join(reversed(f[1]))
normal = "".join(f[0])

mirS = Stack()
norS = Stack()
mirQ = Queue()
mirE = 0
norE = 0
failed = 0
for i in mirror:
    mirS.push(i)
    index = mirS.size()-1
    if mirS.size() >=3 and mirS.items[index] == mirS.items[index-1] and mirS.items[index] == mirS.items[index-2]:
        for x in range(3):
            mirS.pop()
        mirQ.enqueue(i)
        mirE = mirE + 1

trap = False if mirQ.size() == 0 else True

if trap == False:
    for i in normal:
        norS.push(i)
        index = norS.size()-1
        if norS.size()>=3 and norS.items[index] == norS.items[index-1] and norS.items[index] == norS.items[index-2]:
            for x in range(3):
                norS.pop()
            norE = norE + 1
    print("NORMAL :")
    print(norS.size())
    if norS.size() == 0:
        print("Empty")
    else:
        print("".join(reversed(norS.items)))
    print("{} Explosive(s) ! ! ! (NORMAL)".format(norE))
else:
    for i in normal:
        norS.push(i)
        index = norS.size()-1
        if norS.size() >= 3 and norS.items[index] == norS.items[index-1] and norS.items[index] == norS.items[index-2] and mirQ.size() != 0:
            temp = norS.pop()
            norS.push(mirQ.dequeue())
            norS.push(temp)
            index = norS.size() - 1
            if norS.size() >= 3 and norS.items[index] == norS.items[index - 1] and norS.items[index] == norS.items[index - 2]:
                for x in range(3):
                    norS.pop()
                failed = failed + 1
        elif norS.size() >= 3 and norS.items[index] == norS.items[index-1] and norS.items[index] == norS.items[index-2] and mirQ.size() == 0:
            for x in range(3):
                norS.pop()
            norE = norE + 1
    print("NORMAL :")
    print(norS.size())
    if norS.size() == 0:
        print("Empty")
    else:
        print("".join(reversed(norS.items)))
    print("{} Explosive(s) ! ! ! (NORMAL)".format(norE))
    if failed != 0:
        print("Failed Interrupted {} Bomb(s)".format(failed))

print("------------MIRROR------------")
print(": RORRIM")
if mirS.size() == 0:
    print("0")
    print("ytpmE")
else:
    print(mirS.size())
    print("".join(reversed(mirS.items)))
print("(RORRIM) ! ! ! (s)evisolpxE {}".format(mirE))
