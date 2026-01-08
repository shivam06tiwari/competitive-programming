for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = max(a[-1]-min(a),max(a)-a[0])
    for i in range(n):
        s = max(s,a[i-1]-a[i])
    print(s)