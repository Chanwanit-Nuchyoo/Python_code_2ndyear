"""
ตึกลึกลับแห่งหนึ่งเมื่อเดินไปข้างหลังจะมีคนบอกรหัสลับมาจงสร้างฟังชั่นคำนวณรหัส
โดยรหัสจะประกอบไปด้วย english word that have repeat character
เช่น bon("ball") = 48 หรือ bon("aah") = 4

def bon(w):
	### Enter Your Code Here ###
secretCode = input("Enter secret code : ")
print(bon(secretCode))
"""


def bon(w):
    for i in w:
        if(w.count(i)) >= 2:
            return (ord(i)-96)*4

secretCode = input("Enter secret code : ")

print(bon(secretCode.lower()))