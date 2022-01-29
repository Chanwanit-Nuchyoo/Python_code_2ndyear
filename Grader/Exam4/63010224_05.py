r = 0


def mergeSort(inp):
    if len(inp) > 1:
        mid = len(inp) // 2
        left = inp[:mid]
        right = inp[mid:]
        global r

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                inp[k] = left[i]
                i += 1
            else:
                inp[k] = right[j]
                j += 1
            k += 1

            r += 1

        while i < len(left):
            inp[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            inp[k] = right[j]
            j += 1
            k += 1


def printList(inp):
    for i in range(len(inp)):
        print(inp[i], end=" ")
    print()


if __name__ == '__main__':
    print(' *** Merge sort ***')
    inp = [int(i) for i in input('Enter some numbers : ').split(' ')]

    mergeSort(inp)
    print("\nSorted -> ", end='')
    printList(inp)
    print('Data comparison = ', r)