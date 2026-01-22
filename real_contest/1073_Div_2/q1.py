for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        if i%2 == 0:
            b.append([a[i],"R"])
        else:
            b.append([a[i],"B"])
    b.sort()
    for i in range(1,n):
        if b[i][1] == b[i-1][1]:
            print("NO")
            break
    else:
        print("YES")