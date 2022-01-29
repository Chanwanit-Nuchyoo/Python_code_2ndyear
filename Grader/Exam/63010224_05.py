class MyInt:
    def __init__(self, number):
        self.number = number

    def toRoman(self):
        copy = self.number
        answer = ""
        while copy != 0:
            if copy >= 1000:
                answer += "M"
                copy -= 1000
            elif copy >= 900:
                answer +="CM"
                copy -= 900
            elif copy >= 500:
                answer +="D"
                copy -= 500
            elif copy >= 400:
                answer +="CD"
                copy -= 400
            elif copy >= 100:
                answer +="C"
                copy -= 100
            elif copy >= 90:
                answer +="XC"
                copy -= 90
            elif copy >= 50:
                answer +="L"
                copy -= 50
            elif copy >= 40:
                answer +="XL"
                copy -= 40
            elif copy >= 10:
                answer +="X"
                copy -= 10
            elif copy >= 9:
                answer +="IX"
                copy -= 9
            elif copy >= 5:
                answer +="V"
                copy -= 5
            elif copy >= 4:
                answer +="IV"
                copy -= 4
            elif copy >= 1:
                answer +="I"
                copy -= 1
        return answer

    def __add__(self,other):
        return (self.number + other.number)+((self.number + other.number)/2)

print(" *** class MyInt ***")
inp = [int(x) for x in input("Enter 2 number : ").split()]

a = MyInt(inp[0])

b = MyInt(inp[1])

print("{} convert to Roman : {}".format(a.number, a.toRoman()))

print("{} convert to Roman : {}".format(b.number, b.toRoman()))

print("{} + {} = {}".format(a.number,b.number,int(a+b)))

