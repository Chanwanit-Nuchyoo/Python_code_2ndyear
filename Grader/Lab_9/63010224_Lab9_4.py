def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : " + Ans)
else:
    l = list(map(int, l))
    o = []
    s = []
    while len(l) != 0:
        t = l.pop(0)
        s.append(t)
        o.append(t)
        bubbleSort(s)
        mid = len(s) // 2
        res = (s[mid] + s[~mid]) / 2
        print("list = {} : median = {:.1f}".format(o, res))
