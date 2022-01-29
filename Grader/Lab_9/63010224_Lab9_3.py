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


def islowtohigh(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def ishightolow(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            return False
    return True


def isMetadrome(arr):
    q = []
    if not islowtohigh(arr):
        return False

    for i in arr:
        if i in q:
            return False
        else:
            q.append(i)
    return True


def isPlaindrome(arr):
    q = []
    if not islowtohigh(arr):
        return False

    for i in arr:
        if i in q:
            return True
        else:
            q.append(i)
    return False


def isKatadrome(arr):
    q = []
    if not ishightolow(arr):
        return False

    for i in arr:
        if i in q:
            return False
        else:
            q.append(i)
    return True

def isNialpdrome(arr):
    q = []
    if not ishightolow(arr):
        return False

    for i in arr:
        if i in q:
            return True
        else:
            q.append(i)
    return False


def isRepdrome(arr):

    q = arr[0]
    for i in arr:
        if q != i:
            return False
    return True

inp = input("Enter Input : ")
l = [int(x) for x in inp]

if isMetadrome(l):
    print("Metadrome")
elif isRepdrome(l):
    print("Repdrome")
elif isPlaindrome(l):
    print("Plaindrome")
elif isKatadrome(l):
    print("Katadrome")
elif isNialpdrome(l):
    print("Nialpdrome")
else:
    print("Nondrome")