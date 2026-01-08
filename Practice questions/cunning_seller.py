L = []
for _ in range(int(input())):
    n = int(input())
    ans = 0
    l = []
    while n:
        l.append(n%3)
        n = n//3
    for i in range(len(l)):
        ans+= l[i]*((3**(i+1))+i*(3**(i-1)))
    L.append(int(ans))
for ch in L:
    print(ch)
    
    