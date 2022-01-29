"""
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา



A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

P ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty
"""

class Stack:
    def __init__(self):
        self.items = []

    def append(self, j):
        self.items.append(j)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def values(self):
        return self.items


stk = Stack()
str = [x for x in input("Enter Input : ").replace(",", " ").split()]
for i in range(len(str)):
    if str[i] == "A":
        stk.append(str[i+1])
        print("Add = {} and Size = {}".format( str[i+1], stk.size()))
    elif str[i] == "P":
        if stk.size() > 0:
            index = stk.size()-1
            data = stk.pop()
            print("Pop = {} and Index = {}" .format(data, index))
        else:
            print("-1")
if stk.size() > 0:
    print("Value in Stack = " + stk.values().__str__().replace("[","").replace("]","").replace("'","").replace(",",""))
else:
    print("Value in Stack = Empty")

