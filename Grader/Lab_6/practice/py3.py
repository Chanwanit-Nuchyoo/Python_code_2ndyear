def ispalindrome(i, j, inp):
    if i > j:
        return True
    else:
        if inp[i] != inp[j]:
            return False
        return ispalindrome(i + 1, j - 1, inp)


inp = input("Enter Input : ")
print("'" + inp + "'" + ' is palindrome' if ispalindrome(0, len(inp)-1, inp) else "'" + inp + "'" + ' is not palindrome')
