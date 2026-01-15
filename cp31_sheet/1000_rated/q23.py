MAX = 30000
l = [True]*(MAX+1)
l[0] = False
l[1] = False
for i in range(2,int(MAX**0.5)+1):
    if l[i] == True:
        for j in range(i*i,MAX+1,i):
            l[j] = False
primes = []
for i in range(MAX+1):
    if l[i] == True:
        primes.append(i)   
for _ in range(int(input())):
    n = int(input())
    l = 0
    ans = 0
    r = len(primes)-1
    while l<=r:
        m = l + (r-l)//2
        if primes[m]>=n+1:
            ans = primes[m]
            r = m-1
        else:
            l = m+1
    a = ans
    l = 0
    ans = 0
    r = len(primes)-1
    while l<=r:
        m = l + (r-l)//2
        if primes[m]>=a+n:
            ans = primes[m]
            r = m-1
        else:
            l = m+1
    b = ans
    print(1,a,b,a*b)