for _ in range(int(input())):
    s,k,m = map(int,input().split())
    if k > m:
        if s>m:
            print(s-m)
        else:
            print(0)
    elif k == m:
        if s>=k:
            print(m)
        else:
            print(s)
    else:
        d = m//k
        r = m%k
        if s >= k:
            if d%2 == 0:
                print(max(0,s-r))
            else:
                print(max(0,k-r))
        else:
            print(max(0,s-r))
            