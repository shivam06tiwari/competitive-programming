n = int(input())
for i in range(n+1):
    l1 = [" "]*(n-i)
    l2 = [x for x in range(i+1)]
    l3 = [x for x in range(i-1,-1,-1)]
    if i == 0:
        l4 = l1+l2
        print(*l4)
    else:
        l4 = l1+l2+l3
        print(*l4)
for i in range(n):
    l1 = [" "]*(i+1)
    l2 = [x for x in range(n-i)]
    l3 = [x for x in range(n-i-2,-1,-1)]
    if i == n-1:
        l4 = l1+l2
        print(*l4)
    else:
        l4 = l1+l2+l3
        print(*l4)
    