def bubblesort(l, i=0):
    if i > len(l) - 1:
        return l
    l = swap(l, i)
    print(l)
    return bubblesort(l, i + 1)


def swap(l, i, j=0):
    if j > len(l) - 2 - i or l[j] < l[j + 1]:
        return l
    if l[j] > l[j + 1]:
        l[j], l[j + 1] = l[j + 1], l[j]

    return swap(l, i, j + 1)


l = input("Enter your List : ").split(" ")
print("List after Sorted : {}".format(str(bubblesort(l)).replace("'", "")))
