t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    ans = a[0] + min(a[0],a[1])
    print(ans)
