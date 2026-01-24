for _ in range(int(input())):
    n = int(input())
    p = [0]*n
    p[n-1] = 1
    for i in range(1,n-1):
        p[i] = (i+1)^1
    if n%2 == 0:
        p[0] = n 
    else:
        p[0] = n-1
    print(*p)
