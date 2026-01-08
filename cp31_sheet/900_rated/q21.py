for _ in range(int(input())):
    s = input()
    s = s[::-1]
    f2 = 0
    f1 = 0
    c0 = 30
    c25 = 30
    c50 = 30
    c75 = 30
    for i in range(len(s)):
        if s[i] == "0":
            c0 = i
            break
    for i in range(c0+1,len(s)):
        if s[i] == "0" or s[i] == "5":
            f1 = 1
            if s[i] == "0":
                c0 = i-1
                c50 = 50
                break
            else:
                c50 = i-1
                c0 = 50
                break
    if f1 == 0:
        c0 = 50
        c50 = 50
    for i in range(len(s)):
        if s[i] == "5":
            c25 = i
            break
    for i in range(c25+1,len(s)):
        if s[i] == "7" or s[i] == "2":
            f2 = 1
            if s[i] == "7":
                c75 = i-1
                c25 = 50
                break
            else:
                c25 = i-1
                c75 = 50
                break
    if f2 == 0:
        c75 = 50
        c25 = 50
    print(min(c0,c25,c50,c75))