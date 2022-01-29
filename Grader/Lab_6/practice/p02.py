def insertion_sort(l, index=1):
    if index == len(l) - 1:
        return insert(index, l)
    l = insert(index, l)
    return insertion_sort(l, index + 1)


def insert(i, l):
    if i == 0 or int(l[i]) < int(l[i - 1]):
        return l

    if int(l[i]) > int(l[i - 1]):
        l[i], l[i - 1] = l[i - 1], l[i]
    return insert(i - 1, l)


def bubblesort(l, i=0):
    if i > len(l) - 1:
        return l

    l = swap(l, i)

    return bubblesort(l, i + 1)


def swap(l, i, j=0):
    if j > len(l) - 2 - i or l[j] > l[j + 1]:
        return l

    if l[j] < l[j + 1]:
        l[j], l[j + 1] = l[j + 1], l[j]

    return swap(l, i, j + 1)


inp = input("Enter list : ").split(",")
print("List after sorted : {}".format(str(insertion_sort(inp)).replace("'", "")))
