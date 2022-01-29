inp, x = input("Enter Input : ").split("/")
x = list(map(int,x.split(" ")))
inp = list(map(int, inp.split(" ")))

for num in x:
    answer = None
    for i in inp:
        if i > num:
            if answer:
                if i < answer:
                    answer = i
            else:
                answer = i
    if answer:
        print(answer)
    else:
        print("No First Greater Value")



