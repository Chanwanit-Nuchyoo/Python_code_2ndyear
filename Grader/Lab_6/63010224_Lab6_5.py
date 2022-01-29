x = 0
def staircase(n, i):
    if n == 0:
        print("Not Draw!")
        return
    if x > 0:
        if n > 1:
            printUnderScore(x - i)
            printSharp(i)
            print("")
            staircase(n - 1, i + 1)
        elif n == 1:
            printUnderScore(x - i)
            printSharp(i)
            print("")
    if x < 0:
        if n > 1:
            printUnderScore(i - 1)
            printSharp(abs(x)-i+1)
            print("")
            staircase(n - 1, i + 1)
        elif n == 1:
            printUnderScore(i - 1)
            printSharp(abs(x) - i + 1)
            print("")


def printSharp(t):
    if t > 1:
        print("#", end="")
        printSharp(t - 1)
    else:
        print("#", end="")


def printUnderScore(t):
    if t == 0:
        return
    elif t == 1:
        print("_", end="")
    else:
        print("_", end="")
        printUnderScore(t - 1)


x = int(input("Enter Input : "))
staircase(abs(x), 1)
