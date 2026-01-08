import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    k = 0
    for i in range(n):
        d = abs(i-a[i]+1)
        k = math.gcd(k,d)
    print(k)
        
        