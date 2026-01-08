for _ in range(int(input())):
    s = list(input())
    t = input()
    n = len(s)
    m = len(t)
    j = 0
    for i in range(n):
        if j < m:
            if s[i] == t[j]:
                j += 1
            elif s[i] == '?':
                s[i] = t[j]
                j += 1
        if s[i] == '?':
            s[i] = 'a'
    if j == m:
        print("YES")
        print("".join(s))
    else:
        print("NO")
            