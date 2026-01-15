for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    for ch in a:
        if ch in d:
            print("YES")
            break
        else:
            d[ch] = 1
    else:
        print("NO")