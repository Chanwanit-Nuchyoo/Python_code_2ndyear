def gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return abs(gcd(b, a % b))


inp = input("Enter Input : ").split(" ")
if abs(int(inp[0])) < abs(int(inp[1])):
    mn = abs(int(inp[0]))
else:
    mn = abs(int(int(inp[1])))

if int(inp[0]) == 0 and int(inp[1]) == 0:
    print("Error! must be not all zero.")

elif int(inp[0]) == 0:
    if int(inp[1]) < 0:
        print("The gcd of 0 and {} is : {}".format(inp[1], gcd(int(inp[0]), int(inp[1]))))
    else:
        print("The gcd of {} and 0 is : {}".format(inp[1], gcd(int(inp[0]), int(inp[1]))))
elif int(inp[1]) == 0:
    if int(inp[0]) < 0:
        print("The gcd of 0 and {} is : {}".format(inp[0], gcd(int(inp[0]), int(inp[1]))))
    else:
        print("The gcd of {} and 0 is : {}".format(inp[0], gcd(int(inp[0]), int(inp[1]))))
else:
    print("The gcd of {} and {} is : {}".format(inp[0] if abs(int(inp[0])) > abs(int(inp[1])) else inp[1],
                                                inp[0] if abs(int(inp[0])) < abs(int(inp[1])) else inp[1],
                                                gcd(int(inp[0]), int(inp[1]))))
