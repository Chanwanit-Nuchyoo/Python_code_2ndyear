def insertion_sort(arr):
    if (len(arr) == 1):
        return
    k = 0
    for i in range(1, len(arr)):
        j = i
        k += 1
        while (j > 0 and arr[j - 1] > arr[j]):
            if j != i:
                k += 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr,k


print(" *** Insertion sort ***")
list = list(map(int, input("Enter some numbers : ").split(" ")))
answer, round = insertion_sort(list)
print()
print(answer)
print("Data comparison =  {}".format(round))
