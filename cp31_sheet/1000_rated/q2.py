for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = 1
    for ch in a:
        s *= ch
    if k == 2:
        if s%2 != 0:
            print(1)
        else:
            print(0)
    elif k == 3:
        if s%3 != 0:
            mn = 10
            for ch in a:
                if ch < 3:
                    mn = min(3-ch,mn)
                elif ch < 6:
                    mn = min(6-ch,mn)
                elif ch < 9:
                    mn = min(9-ch,mn)
                else:
                    mn = min(12-ch,mn)   
            print(mn)
        else:
            print(0)          
    elif k == 4:
        if s%4 != 0:
            mn = 10
            mnn = 0
            for ch in a:
                if ch%2 ==0:
                    mnn += 1
                if ch < 4:
                    mn = min(4-ch,mn)
                elif ch < 8:
                    mn = min(8-ch,mn)
                else:
                    mn = min(12-ch,mn)  
            if mn == 1:
                print(1)
            else:
                if mnn == 1:
                    print(1)
                else:
                    print(2)
        else:
            print(0)
    else:
        if s%5 != 0:
            mn = 10
            for ch in a:
                if ch < 5:
                    mn = min(5-ch,mn)
                else:
                    mn = min(10-ch,mn) 
            print(mn)
        else:
            print(0)
            
