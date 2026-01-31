for _ in range(int(input())):
    n = int(input())
    l = [0]*n
    l[-1] = n
    z = n//2+1
    x = n//2
    for i in range(n):
        if i%2 == 0:
            l[i] = z
            z += 1
        else:
            l[i] = x
            x -= 1
    print(*l)