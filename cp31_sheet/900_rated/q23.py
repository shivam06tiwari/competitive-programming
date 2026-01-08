for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = a[0]
    for ch in a:
        c = c&ch
    print(c)