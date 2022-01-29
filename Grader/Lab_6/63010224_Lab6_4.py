sA = ['A']
sB = ['B']
sC = ['C']
u = 0


def move(n, A, B, C):
    if (n > 0):
        move(n - 1, A, C, B)
        print("move %d from  %s to %s" % (n, A[0], C[0]))
        ind = A.index(n)
        C.insert(1, A[ind])
        C.pop()
        A[ind] = 0
        charA = A.pop(0)
        charC = C.pop(0)
        A.sort(reverse=True)
        C.sort(reverse=True)
        A.insert(0, charA)
        C.insert(0, charC)
        show_list(u, sA, sB, sC)
        move(n - 1, B, A, C)


def fill_stack(n, A, B, C):
    if n != 0:
        A.append(int(n))
        B.append(int(0))
        C.append(int(0))
        fill_stack(n - 1, A, B, C)
    else:
        A.append(int(0))
        B.append(int(0))
        C.append(int(0))


def show_list(n, A, B, C):
    if n != 0:
        print("{}  {}  {}".format(A[n + 1] if A[n + 1] != 0 else '|', B[n + 1] if B[n + 1] != 0 else '|',
                                  C[n + 1] if C[n + 1] != 0 else '|'))
        show_list(n - 1, A, B, C)
    else:
        print("{}  {}  {}".format(A[n + 1] if A[n + 1] != 0 else '|', B[n + 1] if B[n + 1] != 0 else '|',
                                  C[n + 1] if C[n + 1] != 0 else '|'))


u = n = int(input("Enter Input : "))
fill_stack(n, sA, sB, sC)
show_list(u, sA, sB, sC)
move(n, sA, sB, sC)
