import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    z = 0
    for i in range(n//2):
        z = math.gcd(z,abs(a[i]-a[n-1-i]))
    print(z)
        
    