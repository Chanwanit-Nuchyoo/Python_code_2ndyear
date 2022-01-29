def max(l, m, i=0):
    if i > len(l)-1:
        return m
    if int(l[i]) > m:
        m = int(l[i])
    return max(l, m, i + 1)


inp = input("Enter Input : ").split(" ")
print("Max : {}".format(max(inp,int(inp[0]))))
