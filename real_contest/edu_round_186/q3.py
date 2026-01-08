for _ in range(int(input())):
    n = int(input())
    s1 = list(map(int,input().split()))
    s2 = list(map(int,input().split()))
    s3 = list(map(int,input().split()))
    i = 0
    f1 = 0
    f2 = 0
    c1 = 0
    c2 = 0
    for j in range(n):
        for k in range(n):
            f = 0
            if s2[k] > s1[(k+i)%n]:
                continue
            else:
                f1 = 1
                break
        if f1 == 0:
            c1 += 1
        for k in range(n):
            f = 0
            if s3[k] > s2[(k+i)%n]:
                continue
            else:
                f2 = 1
                break
        if f2 == 0:
            c2 += 1
        i += 1
        f1 = 0
        f2 = 0
    print(c1*c2*n)
                
    