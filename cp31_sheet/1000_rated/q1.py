for _ in range(int(input())):
    s = input()
    s1 = s.count("1")
    s2 = s.count("0")
    f = 0
    for ch in s:
        if ch == "1":
            if s2 == 0:
                print(s1)
                f = 1
                break
            else:
                s2 -= 1
        else:
            if s1 == 0:
                print(s2)
                f = 1
                break
            else:
                s1 -= 1
    if f == 0:
        print(0)
    