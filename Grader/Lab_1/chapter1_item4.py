def odd_list(alist):
    re = [x for x in alist if x % 2 == 1]
    return re


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
