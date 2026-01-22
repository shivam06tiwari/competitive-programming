for _ in range(int(input())):
    n = int(input())
    s = input()
    k = []
    c1 = n//2
    c2 = n//2
    c = 0
    mx = 0
    if s[0] == "(":
        c += 1
    for i in range(1,n):
        if s[i] == ")" and s[i-1] == "(":
            k.append([c,i])
        if s[i] == "(":
            c += 1
    for i in range(len(k)):
        c1 -= k[i][0]
        c2 -= k[i][0]
        for j in range(k[i][1],n):
            if s[j] == "(":
                break
            else:
                c2 -= 1
        if c2 > 0:
            mx = max(n-(c1-c2)*2,mx)
        c1 = n//2
        c2 = n//2
    c1 = n//2
    for i in range(n-1):
        if s[i] == "(":
            c1 -= 1
        if s[i] == ")" and s[i+1] == "(":
            if i != n-1 and c>=2:
                mx = max(n-2,mx)
    if mx <= 0:
        print(-1)
    else:
        print(mx)
    
    