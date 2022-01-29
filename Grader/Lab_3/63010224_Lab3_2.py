"""
Chapter : 3 - item : 2 - Parenthesis Matching
 ส่งมาแล้ว 0 ครั้ง
จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา

โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด

1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด

2. วงเล็บปิดเกิน

3. วงเล็บเปิดเกิน

แล้วให้แสดงผลตามตัวอย่าง
"""
"""
code นี้เป็นเวอร์ชันปรับปรุง อาจไม่เหมือนในเกรดเดอร์ แต่ทำได้ทุกเคสเหมือนกัน แถมสะอาดกว่าเดิม
"""
import sys
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

    def peek(self):
        return self.items[-1]


arg = input("Enter expresion : ")

open_list = ["[","{","("]
close_list = ["]","}",")"]

stack = Stack()

for char in arg:
    if char in open_list:
        stack.push(char)
    elif char in close_list:
        index = close_list.index(char)
        if stack.size() == 0:
            print(arg + " close paren excess")
            sys.exit()
        elif stack.peek() == open_list[index]:
            stack.pop()
        else:
            print(arg + " Unmatch open-close")
            sys.exit()


if stack.size() == 0:
    print(arg + " MATCH")
else:
    print(arg + " open paren excess   {} : {}".format(stack.size(), ''.join(stack.items)))