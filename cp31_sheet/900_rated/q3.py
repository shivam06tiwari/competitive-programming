for _ in range(int(input())):
    n,k,x = map(int,input().split())
    z = n-k
    if x >= ((k*(k+1))//2) and x <= ((n*(n+1))//2) - ((z*(z+1))//2):
        print("YES")
    else:
        print("NO")
        