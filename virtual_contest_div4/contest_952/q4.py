for _ in range(int(input())):
    n,m = map(int,input().split())
    a,b = 0,0
    a = 0
    h = 0
    y = 0
    for i in range(n):
        x = list(input())
        if x.count("#") > a:
            a = x.count("#")
            h = i+1
            if a%2 == 1:
                r = 0
                while x[r] != "#":
                    r += 1
                r += a//2+1  
    print(h,r)
        
    