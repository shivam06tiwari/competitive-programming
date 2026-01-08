for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0
    for i in range(n-1,0,-1):
        while a[i] <= a[i-1]:
            if a[i] == 0 and a[i-1] == 0:
                break
            else:
                a[i-1] //= 2
                c += 1
    f = 0
    for j in range(n-1):
        if a[j] >= a[j+1]:
            f = 1
            break
    if f == 1:
        print(-1)
    else:
        print(c)