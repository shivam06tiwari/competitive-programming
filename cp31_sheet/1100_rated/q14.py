for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = []
    l = 0
    r = 0
    c = 1
    for i in range(n-1):
        if b[i+1] >= b[i]:
            l = i+2
            c += 1
        else:
            if c != 1:
                ans.append([c,l])
                c = 1
    if c != 1:
        ans.append([c,l])
    ans.sort()
    print(ans)
    for ch in ans:
        r = ch[1] - ch[0]
        l = ch[1]
        if a[r:l] != b[r:l]:
            print(r+1,l)
            break