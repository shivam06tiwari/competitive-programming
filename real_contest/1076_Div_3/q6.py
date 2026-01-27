for _ in range(int(input())):
    n,x1,y1,x2,y2 = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    d = len(set(a))
    ans = 0
    c = [[x1,y1]]
    for i in range(n):
        c.append([a[i],b[i]])
    c.append([x2,y2])
    c.sort()
    g = []
    x,ymn,ymx = c[0][0],c[0][1],c[0][1]
    for i in range(1,len(c)):
        if c[i][0] == x:
            ymn = min(ymn,c[i][1])
            ymx = max(ymx,c[i][1])
        else:
            g.append([x,ymn,ymx])
            x,ymn,ymx = c[i][0],c[i][1],c[i][1]
    g.append([x,ymn,ymx])
    p = 0
    q = 0
    u = g[0][0]
    v = g[0][1]
    w = g[0][2]
    for x,ymn,ymx in g[1:]:
        d = x-u
        u = x
        s = ymx-ymn
        pp = min(p+abs(v-ymx),q+abs(w-ymx))+d+s
        qq = min(p+abs(v-ymn),q+abs(w-ymn))+d+s
        p = pp
        q = qq
        u = x
        v = ymn
        w = ymx   
    print(min(p,q))