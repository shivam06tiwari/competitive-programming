for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    c = 0
    mx = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            continue
        if abs(a[i]-a[i+1]) == 1:
            c += 1
            mx = max(c,mx)
        else:
            c = 0
    print(mx+1)