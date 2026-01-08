L = []
c = 0
s = ""

for i in range(1000000):
    if i <= 9:
        c += 1
    else:
        s = str(i+1)
        if s.count("0") == len(s)-1:
            c += 1
    L.append(c)
        
for _ in range(int(input())):
    n = int(input())
    print(L[n-1])

    