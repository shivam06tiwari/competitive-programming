for _ in range(int(input())):
    n = int(input())
    f = 2
    fact = 1
    while f*f <= n:
        if n%f == 0:
            fact = f
            break
        f += 1
    if n%2 == 0:
        print(n//2,n//2)
    elif fact == 1:
        print(1,n-1)
    else:
        print(n//fact,n-n//fact)