import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    m = {}
    s = list(set(a))
    mx = -1
    for i in range(1,n+1):
        m[a[i-1]] = i
    for i in range(len(m)):
        for j in range(i,len(m)):
            z = math.gcd(s[i],s[j])
            if z == 1:
                mx = max(mx,m[s[i]]+m[s[j]])
    print(mx)