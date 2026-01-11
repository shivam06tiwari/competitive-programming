for _ in range(int(input())):
    n,k,b,s = map(int,input().split())
    if s < k*b or s > (k*b)+(k-1)*n:
        print(-1)
    else:
        l = [0]*(n-1)
        l.append(k*b)
        r = s - k*b
        i = 0
        while r > 0:
            l[i] += min(k-1,r)
            r -= min(k-1,r)
            i += 1
        print(*l)
        