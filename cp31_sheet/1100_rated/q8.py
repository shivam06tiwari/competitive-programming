import sys
data = sys.stdin.read().split()
idx = 0
t = int(data[idx])
idx += 1
for _ in range(t):
    n,k,a,b = int(data[idx]),int(data[idx+1]),int(data[idx+2]),int(data[idx+3])
    idx += 4
    l = []
    for i in range(n):
        x,y = int(data[idx]),int(data[idx+1])
        l.append([x,y])
        idx += 2
    x = l[a-1]
    y = l[b-1]
    mnx = 10**18+1
    mny = 10**18+1
    for i in range(k):
        mnx = min(mnx,abs(x[0]-l[i][0])+abs(x[1]-l[i][1]))
        mny = min(mny,abs(y[0]-l[i][0])+abs(y[1]-l[i][1]))  
    mnz = abs(x[0]-y[0])+abs(x[1]-y[1])
    print(min(mnz,(mnx+mny)))
    
# little bit fater using iterator, not much improvement
    
d = map(int,open(0).read().split())
t = next(d)
for _ in range(t):
    n,k,a,b = next(d),next(d),next(d),next(d)
    l = []
    for i in range(n):
        x,y = next(d),next(d)
        l.append([x,y])
    x = l[a-1]
    y = l[b-1]
    mnx = 10**18+1
    mny = 10**18+1
    for i in range(k):
        mnx = min(mnx,abs(x[0]-l[i][0])+abs(x[1]-l[i][1]))
        mny = min(mny,abs(y[0]-l[i][0])+abs(y[1]-l[i][1]))      
    mnz = abs(x[0]-y[0])+abs(x[1]-y[1])
    print(min(mnz,(mnx+mny)))

# little bit more faster using if/else instead of  min/max

import sys
data = sys.stdin.read().split()
idx = 0
t = int(data[idx])
idx += 1
for _ in range(t):
    n,k,a,b = int(data[idx]),int(data[idx+1]),int(data[idx+2]),int(data[idx+3])
    idx += 4
    l = []
    for i in range(n):
        x,y = int(data[idx]),int(data[idx+1])
        l.append([x,y])
        idx += 2
    x = l[a-1]
    y = l[b-1]
    mnx = 10**18+1
    mny = 10**18+1
    x0,x1 = x
    y0,y1 = y
    for i in range(k):
        lx,ly = l[i]
        d1 = abs(x0-lx)+abs(x1-ly)
        if d1 < mnx:
            mnx = d1
        d2 = abs(y0-lx)+abs(y1-ly)
        if d2 < mny: 
            mny = d2
    mnz = abs(x0-y0)+abs(x1-y1)
    if mnz < mnx+mny:
        print(mnz)
    else:
        print(mnx+mny)
        
# Fastest method using binary input and if/else
     
d = map(int,open(0,'rb').read().split())
t = next(d)
for _ in range(t):
    n,k,a,b = next(d),next(d),next(d),next(d)
    l = []
    for i in range(n):
        x,y = next(d),next(d)
        l.append([x,y])
    x = l[a-1]
    y = l[b-1]
    mnx = 10**18+1
    mny = 10**18+1
    x0,x1 = x
    y0,y1 = y
    for i in range(k):
        lx,ly = l[i]
        d1 = abs(x0-lx)+abs(x1-ly)
        if d1<mnx: mnx=d1
        d2 = abs(y0-lx)+abs(y1-ly)
        if d2<mny: mny=d2      
    mnz = abs(x0-y0)+abs(x1-y1)
    print(min(mnz,(mnx+mny)))