for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[0] != 1:
        print("NO")
    else:
        sum = 1
        for i in range(1,n):
            if a[i] > sum:
                print("NO")
                break
            else:
                sum += a[i]
        else:
            print("YES")