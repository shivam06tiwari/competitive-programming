for _ in range(int(input())):
    n = int(input())
    d2 = 0
    d3 = 0
    while n%2 == 0:
        d2 += 1
        n //= 2
    while n%3 == 0:
        d3 += 1
        n //= 3
    if d2>d3 or n != 1:
        print(-1)
    else:
        print(2*d3-d2)    