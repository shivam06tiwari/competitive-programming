for _ in range(int(input())):
    a = list(input())
    b = list(input())
    ca = 1
    cb = 1
    f = 0
    j = 0
    if len(b) < len(a):
        print("NO")
    else:
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                ca += 1
            else:
                cb = 1
                while b[j] == b[j+1]:
                    j += 1
                    cb += 1
                j+=1
                if (cb >= ca) and (cb <= 2*ca):
                    ca = 1
                    continue
                else:
                    f = 1
                    break
        if f == 0:
            print("YES")
        else:
            print("NO")
                    