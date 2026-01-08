for _ in range(int(input())):
    n, k, q = map(int,input().split())
    l = [0]*n
    h = 0
    for i in range(q):
        a = list(map(int,input().split()))
        if a[0] == 1:
            for j in range(a[1]-1,a[2]):
                if j == a[1]-1:
                    l[j] = k
                else:
                    l[j] = k+1
        else:
            for j in range(a[1]-1,a[2]):
                if k == 0:
                    break
                else:
                    if l[j] == 0:
                        l[j] = h
                        h+=1
                        k-=1
    print(*l)
    
    