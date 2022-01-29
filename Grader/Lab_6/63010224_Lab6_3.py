def GCD(m, l):
    if l[0] == 0 and l[1] == 0:
        print("Error! must be not all zero.")
    elif m == 0:
        print("The gcd of {} and {} is : {}".format(max(l), min(l), max(l)))
    elif l[0] % m == 0 and l[1] % m == 0:
        if l[0] < 0 and l[1] < 0:
            print("The gcd of {} and {} is : {}".format(min(l), max(l), m))
        else:
            print("The gcd of {} and {} is : {}".format(max(l), min(l), m))
    else:
        GCD(m - 1, l)


inp = [int(x) for x in input("Enter Input : ").split()]
GCD(abs(min(inp)), inp)
