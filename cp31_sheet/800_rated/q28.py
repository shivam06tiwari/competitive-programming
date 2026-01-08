for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if a.count(a[0]) == n:
        print("NO")
    else:
        print("YES")
        a.sort(reverse=True)
        temp = a[-1]
        a[-1] = a[1]
        a[1] = temp
        print(*a)