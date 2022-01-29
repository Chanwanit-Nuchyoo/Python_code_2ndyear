"""
รับ input เป็น list แล้วแสดงขั้นตอนของ bubble sort ตามตัวอย่าง

***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import***
"""


def optimizedBubbleSort(a):
    update = True
    n = len(a)
    r = 1
    while (update == True and n > 1):
        update = False
        m = None
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                update = True
                m = a[i+1]
        n -= 1
        if update and n > 1:
            print("{} step : {} move[{}]".format(r, a, m))
        else:
            print("last step : {} move[{}]".format(a, m))
        r += 1
    return a


l = [int(x) for x in input("Enter Input : ").split(" ")]
optimizedBubbleSort(l)
