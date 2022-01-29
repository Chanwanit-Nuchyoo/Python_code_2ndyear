def rotate(toomuch,original_message, cloned_message1, cloned_message2, n):
    if n <= 5:
       print("{} {} {}".format(n, "".join(cloned_message1), "".join(cloned_message2)))
    elif n>5 and not toomuch:
        print(" . . . . .")
        toomuch = True
    n+=1
    tail = cloned_message1.pop()
    cloned_message1.insert(0, tail)
    head = cloned_message2.pop(0)
    cloned_message2.append(head)
    if "".join(cloned_message1) == original_message[0] and "".join(cloned_message2) == original_message[1]:
        print("{} {} {}".format(n, "".join(cloned_message1), "".join(cloned_message2)))
        print("Total of  {} rounds.".format(n))
        return
    else:
        rotate(toomuch,original_message, cloned_message1, cloned_message2, n)


print("*** String Rotation ***")
original_message = input("Enter 2 strings : ").split()
cloned_message1 = []
cloned_message2 = []
for i in original_message[0]:
    cloned_message1.append(i)
for i in original_message[1]:
    cloned_message2.append(i)

tail = cloned_message1.pop()
cloned_message1.insert(0, tail)
head = cloned_message2.pop(0)
cloned_message2.append(head)
n=1
toomuch = False
rotate(toomuch,original_message, cloned_message1, cloned_message2,n)
