print(" *** String count ***")
lower_list = []
upper_list = []
ln = 0
un = 0
inp_message = input("Enter message : ")

for i in inp_message:
    if i.islower():
        ln += 1
    elif i.isupper():
        un += 1

    if i.islower() and i not in lower_list:
        lower_list.append(i)
    elif i.isupper() and i not in upper_list:
        upper_list.append(i)

lower_list.sort()
upper_list.sort()

print("No. of Upper case characters : {}".format(un))
print("Unique Upper case characters : {}".format("  ".join(upper_list)))
print("No. of Lower case Characters : {}".format(ln))
print("Unique Lower case characters : {}".format("  ".join(lower_list)))