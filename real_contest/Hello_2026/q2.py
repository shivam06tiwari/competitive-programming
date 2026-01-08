for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = set(a)
    if a.count(0) == n:
        print(1)
    else:
        if a.count(0) == 0:
            print(0)
        else:
            mx = 0
            for i in range(1,k):
                if i in s:
                    mx = i
                else:
                    break
            print(min((mx+1),k-1))
    