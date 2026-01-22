for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mx = max(a)
    c = a[0]
    for i in range(n-1):
        if a[i+1]%2 != a[i]%2:
            c = max(a[i+1],c+a[i+1])
        else:
            c = a[i+1]
        mx = max(mx,c)
    print(mx)
        
    
            
        
        