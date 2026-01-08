for _ in range(int(input())):
    n = int(input())
    a = input()
    i = 0
    c = n
    j = n-1
    while j>i:
        if a[i] == "0" and a[j] == "1" or a[i] == "1" and a[j] == "0":
            n -= 2
            i += 1
            j -= 1
        else:
            break
    print(n)