L = []
for _ in range(int(input())):
    n = int(input())
    a = list(input())
    b = a.copy()
    b.reverse()
    ina = []
    inb = [] 
    cna = 0
    cnb = 0
    mxa = 0
    mxb = 0
    if a.count("a") == 0 or a.count("a") == 1 or a.count("b") == 0 or a.count("b") == 1:
        L.append(0)
    else:
        for i in range(n):
            if a[i] == "a":
                ina.append(i)
            else:
                inb.append(i)
        cna = ina[len(ina)//2]
        cnb = inb[len(inb)//2]
        h = 1
        for ch in ina[0:len(ina)//2]:
            mxa += cna -h - ch
            h += 1
        h = 1
        for ch in ina[(len(ina)//2)+1:len(ina)+1]:
            mxa += ch - cna - h
            h += 1
        h = 1
        for ch in inb[0:len(inb)//2]:
            mxb += cnb -h - ch
            h += 1
        h = 1
        for ch in inb[(len(inb)//2)+1:len(inb)+1]:
            mxb += ch - cnb - h
            h += 1
        L.append(min(mxb,mxa))
for ch in L:
    print(ch)
            
        
        
                
            
                
                
                
        