a = input().strip()
b = input().strip()
v = "aeiou"
flag = 1
if len(a) != len(b):
    flag = 0
else:
    for i in range(len(a)):
        if (a[i] in v) and (b[i] not in v):
            flag = 0
            break
        elif (a[i] not in v) and (b[i] in v):
            flag = 0
            break
        else:
            continue
if flag == 1:
    print("YES")
else:
    print("NO")
    