class node:
    def __init__(self, data =None, next = None ):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data


def createList(l=[]):
    head = None
    for item in l:
        if head is None:
            head = node(item)
        else:
            t = head
            while t.next is not None:
                t = t.next
            t.next = node(item)
    return head

def printList(H):
    t = H
    print("{} ".format(t.data), end="")
    while t.next is not None:
        t = t.next
        print("{} ".format(t.data), end="")

def mergeOrderesList(p,q):
    new_head = p
    t = p
    y = q
    while t.next is not None:
        t = t.next
    while q.next is not None:
        t.next = q
        t = t.next
        q = q.next
    return new_head

def sortList(H):
    # Node current will point to head
    head = H
    current = H;
    index = None;

    if (H == None):
        return;
    else:
        while (current != None):
            # Node index will point to node next to current
            index = current.next;

            while (index != None):
                # If current node's data is greater than index's node data, swap the data between them
                if (current.data > index.data):
                    temp = current.data;
                    current.data = index.data;
                    index.data = temp;
                index = index.next;
            current = current.next;
        return head


            #################### FIX comand ####################
# input only a number save in L1,L2
inp = input("Enter 2 Lists : ").split()
L1 = [int(x) for x in inp[0].split(",")]
L2 = [int(x) for x in inp[1].split(",")]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ', end='')
printList(LL1)
print('\nLL2 : ', end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
m = sortList(m)
print('\nMerge Result : ',end='')
printList(m)