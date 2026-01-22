for _ in range(int(input())):
    n = int(input())
    s = input()
    m = set()
    c = 0
    for i in range(n):
        m.add(s[i])
        c += len(m)
    print(c)
        