for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = set(a)
    c = list(b)
    if len(b) == 1:
        print("Yes")
    elif len(b) == 2:
        if n%2 == 0:
            if a.count(c[0]) == n//2:
                print("Yes")
            else:
                print("No")
        elif a.count(c[0]) == n//2 or a.count(c[0]) == n//2+1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")