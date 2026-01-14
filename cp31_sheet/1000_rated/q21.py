for _ in range(int(input())):
    a = input()
    b = input()
    la = len(a)
    lb = len(b)
    laa = la
    c = 0
    lbb = lb
    if la > lb:
        t = 1
        while lbb:
            for i in range(lb):
                if b[i:t] != "":
                    if b[i:t] in a:
                        c = max(c,len(b[i:t]))
            t += 1
            lbb -= 1
        print(la+lb-2*c)
    if lb >= la:
        t = 1
        while laa:
            for i in range(la):
                if a[i:t] != "":
                    if a[i:t] in b:
                        c = max(c,len(a[i:t]))
            t += 1
            laa -= 1
        print(la+lb-2*c)
                
        
        
            