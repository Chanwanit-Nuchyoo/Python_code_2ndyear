
print(" *** Divisible number ***")
factor_list = []
inp_number = int(input("Enter a positive number : "))
if inp_number <= 0:
    print("{} is OUT of range !!!".format(inp_number))
else:
    for i in range(1,inp_number+1,1):
        if inp_number % i == 0:
            factor_list.append(str(i))
    print("Output ==>{}".format(" "+" ".join(factor_list)))
    print("Total ==> {}".format(len(factor_list)))

