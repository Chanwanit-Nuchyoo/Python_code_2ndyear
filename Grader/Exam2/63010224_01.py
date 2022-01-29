class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        message = "Data in Stack is : " + str(self.list).replace("[","").replace("]","").replace(",","")
        return message

    def push(self, data):
        self.list.append(data)

    def isEmpty(self):
        return len(self.list) == 0

    def peek(self):
        return self.list[-1]

    def bottom(self):
        return self.list[0]

    def size(self):
        return len(self.list)

    def pop(self):
        return self.list.pop()


choice = input("Enter choice : ")
if choice == '1':
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :", s1.peek())
    print("Bottom of stack :", s1.bottom())
elif choice == '2':
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :", s1.isEmpty())
elif choice == '3':
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :", s1.size())
