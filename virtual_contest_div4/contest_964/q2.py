for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    s = 0
    if (a>c and b>=d) or (a>=c and b>d):
        s += 2
    if (a>d and b>=c) or (a>=d and b>c):
        s += 2 
    print(s)
        
    
        