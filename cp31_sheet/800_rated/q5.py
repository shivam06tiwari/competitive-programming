for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mx = max(a)
    mn = min(a)
    if a[0] != mn:
        print("No")
    else:
        print("Yes")