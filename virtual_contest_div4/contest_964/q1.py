for _ in range(int(input())):
    l,r = map(int,input().split())
    s = 0
    z = 0
    y = 0
    m = 0
    for i in range(12,-1,-1):
        if l>=3**i:
            s = i
            m = i+1
            break
        else:
            continue
    x = 0
    while x != s:
        y += (x+1)*(3**(x+1)-3**x)
        x += 1
    x+1
    y += (x+1)*(l-3**x)
    for i in range(12,-1,-1):
        if r>=3**i:
            s = i
            break
        else:
            continue
    x = 0
    while x != s:
        z += (x+1)*(3**(x+1)-3**x)
        x += 1
    x+1
    z += (x+1)*(r+1-3**x)
    print(z-y+m)
    
    
    