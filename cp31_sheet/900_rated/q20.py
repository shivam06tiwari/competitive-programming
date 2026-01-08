for _ in range(int(input())):
    s = input()
    cab = 0
    cba = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if s[i] == "a":
                cab += 1
            else:
                cba += 1
    if abs(cab-cba) == 1:
        if s[0] == "a":
            s = "b"+s[1:]
        else:
            s = "a"+s[1:]
        print(s)
    elif cab != cba:
        i = 0
        while s[i] == s[i+1]:
            i += 1
        i += 1
        j = len(s)-1
        k = 1
        while s[j] == s[j-1]:
            k += 1
            j -= 1
        if k >= i:
            if s[0] == "a":
                s = ("b"*i)+s[i:]
            else:
                s = ("a"*i)+s[i:]
        else:
            if s[-1] == "a":
                s = s[0:len(s)-k]+("b"*k)
            else:
                s = s[0:len(s)-k]+("a"*k)
        print(s)
    else:
        print(s)