from decimal import Decimal as D
class Stack():

    def __init__(self, *ls):
        self.items = [x for x in ls]

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def postFixeval(st):

    s = Stack()
    for i in st:
        if(i not in "+-*/"):
            s.push(i)
        else:
            operator = i
            y = D(s.pop())
            x = D(s.pop())
            if operator == "+":
                s.push(x+y)
            elif operator == "-":
                s.push(x-y)
            elif operator == "*":
                s.push(x*y)
            elif operator == "/":
                s.push(x/y)
    return s.pop()


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))
