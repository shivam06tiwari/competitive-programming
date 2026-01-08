L = []
for _ in range(int(input())):
    a = int(input())
    if a%2 != 0:
        L.append(0)   
    elif a == 0:
        L.append(0)
    else:
        L.append(a//4 + 1)    
for ch in L:
    print(ch)