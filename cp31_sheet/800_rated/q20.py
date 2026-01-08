for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    n += 1
    for i in range(n-2):
        print(n-a[i],end=" ")
    print(n-a[-1])