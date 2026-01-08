n=int(input())
N=[]
for i in range(n):
    t=int(input())
    M=[]
    for j in range(t):
        count=0
        code=input()
        for ch in code:
            if ch == "#":
                count+=1
                break
            else:
                count+=1
        M.append(count)
    M.reverse()
    N.append(M)
for l in N:
    for n in l:
        print(f"{n} ",end="")
    print()        