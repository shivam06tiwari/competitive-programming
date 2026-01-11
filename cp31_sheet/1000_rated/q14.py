for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    f = 0
    for i in range(n):
        c = 0
        if i > 0 and s[i] == s[i-1]: 
            c = 1
        if i < n-1 and s[i] == s[i+1]: 
            c = 1
        if c == 0:
            f = 1
            break
    if f == 0:
        l = []
        i = 0
        while i < n:
            j = i
            while j < n-1 and s[j+1] == s[i]:
                j += 1
            l1 = list(range(i+2,j+2))
            l2 = [i+1]
            l += l1+l2
            i = j+1
        print(*l)
    else:
        print(-1)