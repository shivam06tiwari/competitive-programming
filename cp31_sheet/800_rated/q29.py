for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0
    x = 0
    for i in range(n-1):
        x = a[i]%2
        if a[i+1]%2 == x:
            c += 1
        else:
            continue
    print(c)