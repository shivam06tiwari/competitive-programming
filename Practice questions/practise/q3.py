for _ in range(int(input())):
    n,k = map(int,input().split())
    l = ["+"]*n
    a = input()
    x = a.count("1")
    y = a.count("0")
    z = a.count("2")
    if n == k:
        l = ["-"]*n
        for ch in l:
            print(ch,end="")
        print()
    else:
        for i in range(x):
            l[n-1-i] = "-"
        for i in range(y):
            l[i] = "-"
        for i in range(z):
            m = y
            n = n-x-1
            while n>=m and z!=0:
                if l[m] != "-":
                    l[m] = "?"
                if l[n] != "-":
                    l[n] = "?"
                m += 1
                n -= 1
                z-=1
        for ch in l:
            print(ch,end="")
        print()
    