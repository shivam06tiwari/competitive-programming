for _ in range(int(input())):
    x,y = input().split()
    x = int(x)
    s = input()
    s = 2*s
    l = []
    g = 0
    b = 0
    for ch in s:
        if ch == "g":
            l.append(b)
            b = 0
            g = 0
        else:
            if ch == y:
                if g != 1:
                    g = 1
                    b += 1
                else:
                    b += 1        
            else:
                if g == 1:
                    b += 1
    print(max(l))
        
                
        
            
            