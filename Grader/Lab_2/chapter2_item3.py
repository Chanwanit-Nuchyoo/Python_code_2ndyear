"""
ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการสร้าง range() ใหม่ขึ้นมาโดยใช้ function แค่ 1 function

ถ้าหากเป็น 1 argument -> range(a)            | start = 0 , end = a , step = 1

ถ้าหากเป็น 2 argument -> range(a, b)        | start = a , end = b , step = 1

ถ้าหากเป็น 3 argument -> range(a, b, c)    | start = a , end = b , step = c
"""
from decimal import Decimal as D


def number_range(args):
    x = []
    i = 0.0
    if len(args) == 1:
        while i < args[0]:
            x.append(i)
            i += 1
    elif len(args) == 2:
        i = args[0]
        while i < args[1]:
            x.append(i)
            i += 1
    else:
        i = args[0]
        while i < args[1]:
            x.append(i)
            i += args[2]
    return x


print("*** New Range ***")
li = [D(x) for x in input("Enter Input : ").split()]
li = [float(x) for x in number_range(li)]

print(str(li).replace("[", "(").replace("]", ")"))

