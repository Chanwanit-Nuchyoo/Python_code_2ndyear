def harmonic_sum(n, i=1, sum=0):
    if i == n:
        if n != 1:
            print("1/{} = ".format(i), end="")
        else:
            print("1 = ".format(i), end="")
        return 1.0 / i

    if i != 1:
        print("1/{} + ".format(i), end="")
    else:
        print("1 + ", end="")
    return 1.0 / i + harmonic_sum(n, i + 1)


print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : "))
print("%.8f" % (harmonic_sum(num)))
