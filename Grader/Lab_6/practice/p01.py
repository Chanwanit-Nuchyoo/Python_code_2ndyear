def print1ToN(n, cur=1):
    if cur == n:
        return str(cur) + " "

    return str(cur) + " " + print1ToN(n, cur + 1)


def printNTo1(n):
    if n == 1:
        return str(n) + " "

    return str(n) + ' ' + printNTo1(n - 1)


print(print1ToN(6) + printNTo1(6))
