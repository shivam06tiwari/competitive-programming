for _ in range(int(input())):
    w,h = map(int,input().split())
    x1 = list(map(int,input().split()))
    x2 = list(map(int,input().split()))
    x1 = sorted(x1[1:])
    x2 = sorted(x2[1:])
    y1 = list(map(int,input().split()))
    y2 = list(map(int,input().split()))
    y1 = sorted(y1[1:])
    y2 = sorted(y2[1:])
    mxx = max(x1[-1]-x1[0],x2[-1]-x2[0])
    mxy = max(y1[-1]-y1[0],y2[-1]-y2[0])
    mxx *= h
    mxy *= w
    print(max(mxx,mxy))