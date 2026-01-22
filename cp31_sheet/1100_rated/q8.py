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