n,k,m = map(int,input().split())
if k%n == 0:
    if m == 1 or m == n:
        print(k//n+2)
    else:
        print(k//n)
else:
    print(k//n+1)