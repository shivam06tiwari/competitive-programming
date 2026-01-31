for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = set(a)
    for ch in a:
        if ch-k in s:
            print("YES")
            break
    else:
        print("NO")