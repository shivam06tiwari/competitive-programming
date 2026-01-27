m = 300001
d = {}
d[1] = {1:1}
for i in range(2,m+1):
    if i not in d:
        for j in range(i,m+1,i):
            k = j
            if j not in d:
                d[j] = {}
            while k%i == 0:
                if i in d[j]:
                    d[j][i] += 1
                else:
                    d[j][i] = 1
                k //= i

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = set(a)
    l = []
    for i in range(1,n+1):
        if i in s:
            l.append(1)
        else:
            ans  = 0
            z = d[i]
            for r,t in z.items():
                if r in s:
                    ans += t
                else:
                    ans = -1
                    break
            l.append(ans)
    print(*l)

            