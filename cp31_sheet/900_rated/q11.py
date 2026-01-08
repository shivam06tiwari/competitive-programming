for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    i = 0
    for i in range(n):
        if a[i] == 1:
            a[i] = 2
    for i in range(n-1):
        if a[i+1]%a[i] == 0:
            a[i+1] += 1
        i += 1
    print(*a)