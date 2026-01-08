for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = a.count(2)
    k = 0
    f = 0
    for i in range(n-1):
        if a[i] == 2:
            k += 1
            c -= 1
        if k == c:
            print(i+1)
            f = 1
            break
    if f == 0:
        print(-1)
        
        