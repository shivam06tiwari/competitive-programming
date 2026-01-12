for _ in range(int(input())):
    n = int(input())
    if n <= 2:
        print(n)
    else:
        if n%2 == 0:
            print(0)
        else:
            print(1)