for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    o = 0
    if k == n-1:
        print("YES")
    else:
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        for i,v in d.items():
            if v%2 != 0:
                o += 1
        if o > k+1:
            print("NO")
        else:
            print("YES")
                    