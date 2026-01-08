L = []
for _ in range(int(input())):
    n = list(input())
    b = ""
    for i in range(len(n)-1,-1,-1):
        if n[i] == "p":
            b = b+"q"
        elif n[i] == "q":
            b = b+"p"
        else:
            b = b+"w"
    L.append(b)
for ch in L:
    print(ch)