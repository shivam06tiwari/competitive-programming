
n,d = map(int,input().split())
a = list(map(int,input().split()))
t = 0
a.sort()
z = n-1
i = 1
while n>=i:
    j=z
    while j >= 0 and i*a[j] > d:
        if n<i:
            break
        j-=1
        t+=1
        n-=i
        a.pop()
        z-=1
        print(j)
    i += 1
print(t)
    