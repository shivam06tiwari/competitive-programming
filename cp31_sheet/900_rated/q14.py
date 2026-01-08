for _ in range(int(input())):
    n = int(input())
    x = 0
    y = 0
    if n%2 != 0 or n < 4:
        print(-1)
    else:
        print(n//4,(n+5)//6)