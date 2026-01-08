for _ in range(int(input())):
    n = int(input())
    f = 0
    i = 1
    while f == 0:
        if n%i != 0:
            f = 1
        i += 1
    print(i-2)
    
    