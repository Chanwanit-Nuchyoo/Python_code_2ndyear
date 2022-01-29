class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,i):
        self.items.append(i)
        print(len(self.items))

    def dequeue(self):
        if len(self.items) > 0:
            x = self.items.pop(0)
            print(x,0)
        else:
            print(-1)

arg = input("Enter Input : ")
arg = arg.replace(","," ")
arg = arg.split()

q = Queue()

for items in range(len(arg)):
    if arg[items] == "E":
        q.enqueue(arg[items+1])
    elif arg[items] == "D":
        q.dequeue()

if len(q.items) == 0:
    print("Empty")
else:
    print(" ".join(q.items))