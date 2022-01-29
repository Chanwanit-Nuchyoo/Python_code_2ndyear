"""
จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 0 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***
"""
from itertools import combinations as cb

number = [int(x) for x in input("Enter Your List : ").split()]
if len(number) > 2:
    number = list(cb(number, 3))
    ans = []
    for item in number:
        if sum(item) == 0 and item not in ans:
            ans.append(item)
    print(str(ans).replace("(","[").replace(")","]"))
else:
    print("Array Input Length Must More Than 2")