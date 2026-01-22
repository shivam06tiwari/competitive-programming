for _ in range(int(input())):
    n = int(input())
    while True:
        z = str(n)
        for ch in z:
            d = int(ch)
            if d > 1 and n%d != 0:
                break
        else:
            print(n)
            break
        n+=1