L =[]
for _ in range(int(input())):
    n, x, y = map(int,input().split())
    a = input().strip()
    if x==0 and y==0:
        L.append("YES")
    else:
        for i in range(n-1,-1,-1):
            if x==0 and y==0:
                break
            if a[i] == "4":
                if x>=0 and y>=0:
                    if x>=y:
                        x-=1
                    else:
                        y-=1
                elif x>=0 and y<0:
                    if x>=(-y):
                        x-=1
                    else:
                        y+=1
                elif x<0 and y>=0:
                    if (-x)>=y:
                        x+=1
                    else:
                        y-=1
                else:
                    if(-x)>=(-y):
                        x+=1
                    else:
                        y+=1
            else:
                if x>0:
                    x-=1
                elif x<0:
                    x+=1
                if y>0:
                    y-=1
                elif y<0:
                    y+=1
        if x==0 and y ==0:
            L.append("YES")
        else:
            L.append("NO")
for ch in L:
    print(ch)
