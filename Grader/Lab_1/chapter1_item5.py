inp = [int(x) for x in input("Enter All Bid : ").split()]
highest = max(inp)
count_highest = inp.count(highest)
s = []
for i in inp:
    if i not in s:
        s.append(i)
s.sort()
if len(inp) == 1:
    print("not enough bidder")
elif count_highest > 1:
    print("error : have more than one highest bid")
else:
    print("winner bid is", s[len(s)-1], "need to pay", s[len(s)-2])
