def sort(l):
    if len(l) <= 1:
        return l
    else:
        return sort([e for e in l[1:] if e >= l[0]]) + [l[0]] +\
            sort([e for e in l[1:] if e < l[0]])


n = [int(x) for x in input("Enter your List : ").split(" ")]
n = sort(n)
print("List after Sorted : {}".format(n))
