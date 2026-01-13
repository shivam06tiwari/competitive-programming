for _ in range(int(input())):
    n = int(input())
    if n <= 2:
        print(n)
    else:
        if n%2 == 0:
            print(0)
        else:
            if n == 3:
                print(3)
            else:
                print(1)