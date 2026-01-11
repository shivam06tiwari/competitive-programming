for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    t = k*"B"
    if t in s:
        print(0)
    else:
        mnn = 200001
        mn = 0
        i = 0
        j = 0
        while i<n-k:
            j = i
            mn = 0
            while j<i+k:
                if s[j] == "W":
                    mn += 1
                j += 1
            if mnn > mn:
                mnn = mn
            i += 1
        if n-k == 0:
            print(s.count("B"))
        else:
            print(mnn)
                
                
                
                
                
                
                
                