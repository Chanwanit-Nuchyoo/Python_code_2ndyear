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

myQueue = Queue()
herQueue = Queue()
info = Queue()
s = input("Enter Input : ").replace(","," ").replace(":", " ").split()
act_dict = {
    "0": "Eat",
    "1": "Game",
    "2": "Learn",
    "3": "Movie"
}

place_dict = {
    "0": "Res.",
    "1": "ClassR.",
    "2": "SuperM.",
    "3": "Home"
}
for act in s:
    info.enqueue(act)

while not info.isEmpty():
    myQueue.enqueue(info.dequeue())
    myQueue.enqueue(info.dequeue())
    herQueue.enqueue(info.dequeue())
    herQueue.enqueue(info.dequeue())

my = "My   Activity:Location = "
your = "Your Activity:Location = "
mq = "My   Queue = "
hq = "Your Queue = "
for i in range(myQueue.size()//2):
    m_act = myQueue.dequeue()
    m_p = myQueue.dequeue()
    h_act = herQueue.dequeue()
    h_p = herQueue.dequeue()
    my = my + "{}:{}, ".format(act_dict[m_act], place_dict[m_p])
    your = your + "{}:{}, ".format(act_dict[h_act], place_dict[h_p])

    mq = mq + "{}:{}, ".format(m_act, m_p)
    hq = hq + "{}:{}, ".format(h_act, h_p)
    myQueue.enqueue(m_act)
    myQueue.enqueue(m_p)
    herQueue.enqueue(h_act)
    herQueue.enqueue(h_p)

print("{}\n{}".format(mq[:-2],hq[:-2]))
print("{}\n{}".format(my[:-2], your[:-2]))

point = 0
for x in range(myQueue.size()//2):
    my_act = myQueue.dequeue()
    my_place = myQueue.dequeue()
    her_act = herQueue.dequeue()
    her_place = herQueue.dequeue()
    if my_act == her_act and my_place == her_place:
        point = point + 4
    elif my_act != her_act and my_place == her_place:
        point = point + 2
    elif my_act == her_act and my_place != her_place:
        point = point + 1
    else:
        point = point - 5

if point >= 7:
    print("Yes! You're my love! : Score is {}.".format(point))
elif point > 0 and point < 7:
    print("Umm.. It's complicated relationship! : Score is {}.".format(point))
else:
    print("No! We're just friends. : Score is {}.".format(point))