for _ in range(int(input())):
    a, b = map(int,input().split())
    n = list(map(int,input().split()))
    m = list(map(int,input().split()))
    x = min(m)
    y = max(m)
    if a == 1:
        print("YES")
    else:
        for i in range(a):
            if x-n[i] < n[i]:
                if i == 0:
                    n[i] = x-n[i]
                else:
                    if x-n[i] >= n[i-1]:
                        n[i] = x-n[i]
        if n == sorted(n):
            print("YES")
            print(n)
        else:
            for i in range(a-1):
                if n[i+1] >= n[i]:
                    continue
                else:
                    if y-n[i+1] > n[i+1]:
                        n[i+1] = y-n[i+1]
            if n == sorted(n):
                print("YES")
            else:
                print("NO")
            print(n)