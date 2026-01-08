for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    f = 0
    x,y,z = 0,0,0
    for i in range(n-2):
        if a[i+1]>a[i]:
            d[a[i+1]] = i+1
    for ch,cj in d.items():
        if f == 1:
            break
        while cj < n:
            if ch > a[cj]:
                f = 1
                z = cj
                y = d[ch]
                x = d[ch]-1
                break
            else:
                cj += 1
    if f == 1:
        print("YES")
        print(x+1,y+1,z+1)
    else:
        print("NO")
        
    