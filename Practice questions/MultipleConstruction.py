t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    ans = [0] * (2 * n)
    pos = 0
    for x in range(n, 0, -1):
        while True:
            if pos + x < 2 * n and ans[pos] == 0 and ans[pos + x] == 0:
                ans[pos] = x
                ans[pos + x] = x
                break
            pos += 1
    print(" ".join(map(str, ans)))
