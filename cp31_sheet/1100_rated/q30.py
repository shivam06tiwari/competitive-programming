for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    x = -1
    y = -1
    l = 0
    r = n-1
    f = 0
    for i in range(n//2):
        if a[l] != a[r]:
            x = a[l]
            y = a[r]
            break
        l += 1
        r -= 1
    else:
        print("YES")
        f = 1
    if f == 0:
        l = 0
        r = n-1
        while l<r:
            if a[l] == x:
                l += 1
            elif a[r] == x:
                r -= 1
            else:
                if a[l] != a[r]:
                    f = 1
                    break
                else:
                    l += 1
                    r -= 1
        if f == 0:
            print("YES")
        else:
            f = 0
            l = 0
            r = n-1
            while l<r:
                if a[l] == y:
                    l += 1
                elif a[r] == y:
                    r -= 1
                else:
                    if a[l] != a[r]:
                        f = 1
                        break
                    else:
                        l += 1
                        r -= 1
            if f == 0:
                print("YES")
            else:
                print("NO")