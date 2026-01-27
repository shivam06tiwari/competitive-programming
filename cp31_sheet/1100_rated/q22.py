for _ in range(int(input())):
    n = int(input())
    ans = (n-1)*(n)*(n+1)*2022//3 + (n*(n+1)*(2*n+1)*2022//6)
    print(ans%(10**9+7))