for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    pm = 0
    m = 0
    for i in range(1,n):
        while pm in a[:i]:
            pm += 1
        while m in a[i:]:
            m += 1
        if pm == m:
            print("NO")
            break
        m = 0
        pm = 0
    else:
        print("YES")
            