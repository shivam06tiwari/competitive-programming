for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    t = []
    for i in range(1,n+1):
        t.append([a[i-1],i])
    t.sort(reverse=True)
    ans = [0]*(n+1)
    time = 0
    for i in range(n):
        v,j = t[i]
        d = i//2+1
        time += 2*d*v
        if i%2 == 0:
            ans[j] = d
        else:
            ans[j] = -d
    print(time)
    print(*ans)