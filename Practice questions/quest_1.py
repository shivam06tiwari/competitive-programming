for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = set(a)
    count = 0
    for ele in b:
        if a.count(ele) >= ele:
            while (a.count(ele) != ele):
                a.remove(ele)
                count += 1
        else:
            while (a.count(ele) != 0):
                a.remove(ele)
                count += 1
    print(count)