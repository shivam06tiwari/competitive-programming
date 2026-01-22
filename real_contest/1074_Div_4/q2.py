for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = max(a)
    print(s*n)