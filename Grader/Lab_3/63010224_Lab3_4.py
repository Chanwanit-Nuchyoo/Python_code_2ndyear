from decimal import Decimal as D
import sys
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


class StackCalc:

    def __init__(self):
        self.stk = Stack()

    def run (self,arg):
        s = arg.split()
        for i in s:
            if i not in "+-*/" and i not in ["DUP", "POP", "PSH"]:
                self.stk.push(i)
            elif i in "+-*/":
                try:
                    x = D(self.stk.pop())
                    y = D(self.stk.pop())
                    if i == "+":
                        self.stk.push(x+y)
                    elif i == "-":
                        self.stk.push(x-y)
                    elif i == "*":
                        self.stk.push(x*y)
                    elif i == "/":
                        self.stk.push(x/y)
                except:
                    print("Invalid instruction: " + arg[0])
                    sys.exit(1)
            else:
                if i =="DUP":
                    self.stk.push(self.stk.peek())
                elif i == "POP":
                    self.stk.pop()

    def getValue(self):
        if self.stk.size() > 0:
            return self.stk.pop()
        else:
            return 0
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())