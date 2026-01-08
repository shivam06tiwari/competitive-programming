for _ in range(int(input())):
    a,b = input().split()
    c = list(a)
    d = list(b)
    e = a[0]
    c[0] = b[0]
    d[0] = e
    for ch in c:
        print(ch,end="")
    print(" ",end="")
    for ch in d:
        print(ch,end="")
    print()