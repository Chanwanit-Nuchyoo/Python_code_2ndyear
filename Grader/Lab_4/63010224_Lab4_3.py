import math
class Queue:
    def __init__(self, ls):
        self.items = list(ls.strip())
    def enqueue(self,i):
        self.items.append(i)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def size(self):
        return len(self.items)

def encodemsg(q1:Queue, q2:Queue):
    i = q1.size()
    for a in range(i):
        x = q1.dequeue()
        y = q2.dequeue()
        if x.islower():
            x = ord(x) - ord('a')
            x = x + int(y)
            x = (x % 26) + ord('a')
            x = chr(x)
        elif x.isupper():
            x = ord(x) - ord('A')
            x = x + int(y)
            x = (x % 26) + ord('A')
            x = chr(x)
        q1.enqueue(x)
        q2.enqueue(y)

def decodemsg(q1:Queue, q2:Queue):
    i = q1.size()
    for a in range(i):
        x = x = q1.dequeue()
        y = q2.dequeue()
        if x.islower():
            x = ord(x) - ord('z')
            x = abs(x - int(y))
            x =  ord('z') - (x%26)
            x = chr(x)
        elif x.isupper():
            x = ord(x) - ord('Z')
            x = abs(x - int(y))
            x = ord('Z') - (x%26)
            x = chr(x)
        q1.enqueue(x)
        q2.enqueue(y)

arg= [x for x in input("Enter String and Code : ").split(",")]

q1 = Queue(arg[0].replace(" ", ""))
q2 = Queue(arg[1].replace(" ", ""))

encodemsg(q1, q2)
print("Encode message is : ",q1.items)
q2 = Queue(arg[1].replace(" ", ""))
decodemsg(q1, q2)
print("Decode message is : ",q1.items)