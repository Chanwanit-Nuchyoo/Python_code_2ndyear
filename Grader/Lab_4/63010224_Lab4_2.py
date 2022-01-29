class Queue:
    def __init__(self, *ls):
        self.items = [x for x in ls]

    def enqueue(self,i):
        self.items.append(i)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def size(self):
        return len(self.items)


arg = input("Enter people and time : ").split()
q = Queue()
q1 = Queue()
q2 = Queue()
for char in arg[0]:
    q.enqueue(char)
i = int(arg[1])
x = 1
timer1 = 0
timer2 = 0
while x <= i:

    if timer1 == 3:
        q1.dequeue()
        timer1 = 0

    if timer2 == 2:
        q2.dequeue()
        timer2 = 0

    if q1.size()<5 and q.size() != 0:
        q1.enqueue(q.dequeue())
    elif q2.size()<5 and q.size() != 0:
        q2.enqueue(q.dequeue())

    timer1 = timer1 + 1
    timer2 = timer2 + 1
    if q1.size() == 0:
        timer1 = 0
    if q2.size() == 0:
        timer2 = 0
    print("{} {} {} {}".format(x,q.items,q1.items,q2.items))
    x = x+1
