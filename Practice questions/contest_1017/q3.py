L = []
for _ in range(int(input())):
    n = int(input())
    valid = [x for x in range(1,2*n+1)]
    ans = [0]
    for i in range(n):
        a = list(map(int,input().split()))
        if i != n-1:
            ans.extend([a[i],a[i+1]])
            valid.remove(a[i])
            valid.remove(a[i+1])
        else:
            ans.append(a[i])
            valid.remove(a[i])
            ans[0] = valid[0]
    L.append(ans)
for ch in L:
    print(*ch)