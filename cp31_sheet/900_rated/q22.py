for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s1 = a.count(1)
    s2 = a.count(0)
    c = s1*(s2**2)
    print(c)