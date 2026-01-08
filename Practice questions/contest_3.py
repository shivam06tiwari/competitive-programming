
n = int(input())
L = []
for i in range(n):
    count = 0
    s = 0
    found = False
    a = input()
    b = input()
    b = list(b)
    a = list(a)
    if len(a) > len(b):
        s = len(b)
    else:
        s = len(a)
    for i in range(s):
        if a[i] == b[i]:
            count += 1
            found = True
        else:
            break
    y = len(a) - count
    z = len(b) - count
    count += z
    count += y
    if found == True:
        count += 1
    L.append(count)
for num in L:
    print(num)