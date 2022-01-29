class Queue:
    def __init__(self):
        self.list = []

    def enQueue(self, data):
        self.list.append(data)

    def deQueue(self):
        return self.list.pop(0)

    def isDuplicate(self):
        q1 = []
        for i in range(len(self.list)):
            if self.list[i] not in q1:
                q1.append(self.list[i])
            else:
                return "Duplicate"
        return "NO Duplicate"


data, command = input("Enter Input : ").split("/")
data = data.split(" ")
q = Queue()
for i in data:
    q.enQueue(i)
command = command.split(",")
for i in range(len(command)):
    if command[i] != "D":
        c, d = command[i].split(" ")
    else:
        c = command[i]
    if c == "E":
        q.enQueue(d)
    elif c == "D":
        q.deQueue()
print(q.isDuplicate())
