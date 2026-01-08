a,b,c = map(int,input().split())
if max(a,b,c) - min(a,b,c) >= 10:
    print("check again")
else:
    l = [a,b,c]
    l.sort()
    print("final "+str(l[1]))