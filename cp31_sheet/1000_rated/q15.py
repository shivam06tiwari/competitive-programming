for _ in range(int(input())):
    n, k = map(int,input().split())
    s = input()
    c = s[:k].count('W')
    mn = c
    for i in range(k,n):
        if s[i] == 'W':
            c += 1
        if s[i-k] == 'W':
            c -= 1
        if c < mn:
            mn = c
    print(mn)