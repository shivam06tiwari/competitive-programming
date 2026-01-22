import math
for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if a.count(a[0]) == n:
        print(0)
    else:
        c = 0
        i = 0
        j = n-1
        while j>=i and abs(a[i]-a[j]) == 0:
            i += 1
            j -= 1
            c += 1
        z = abs(a[i]-a[j])
        for i in range(c,n//2-c):
            z = math.gcd(z,abs(a[i]-a[n-i-1]))
        print(z)
            
        
    