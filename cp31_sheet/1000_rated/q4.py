for _ in range(int(input())):
    al= 10e9
    bl = 10e9
    s = 0
    n = int(input())
    for i in range(n):
        n1 = int(input())
        a = list(map(int,input().split()))
        a.sort()
        if a[0] < al:
            al = a[0]
        s += a[1]
        if a[1] < bl:
            bl = a[1]
    s += al
    s -= bl
    print(s)
            
        