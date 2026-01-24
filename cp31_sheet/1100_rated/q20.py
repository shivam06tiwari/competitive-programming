import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s1 = a[0]
    s2 = sum(a)-a[0]
    mx = math.gcd(s1,s2)
    for i in range(n-2):
        s1 += a[i+1]
        s2 -= a[i+1]
        z = math.gcd(s1,s2)
        mx = max(z,mx)
    print(mx)