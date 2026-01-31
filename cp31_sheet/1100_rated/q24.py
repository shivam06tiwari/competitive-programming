for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = -1
    for i in range(n):
        if a[i] != i:
            if ans == -1:
                ans = i
            else:
                ans &= i
    print(ans)