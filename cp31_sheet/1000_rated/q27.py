for _ in range(int(input())):
    n = int(input())
    while True:
        z = str(n)
        for ch in z:
            if int(ch) != 1 and int(ch) != 0 and n%int(ch) != 0:
                break
        else:
            print(n)
            break
        n+=1