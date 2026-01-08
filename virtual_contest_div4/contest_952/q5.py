for _ in range(int(input())):
    x,y,z,k = map(int,input().split())
    L = []
    mx = 0
    mxx  = 0
    for i in range(x,0,-1):
        if k%i == 0:
            for j in range(y,0,-1):
                if k%j == 0:
                    if i*j > k:
                        continue
                    else:
                        l = k//(i*j)
                        if i*j*l == k and l<=z:
                            mx = (x-i+1)*(y-j+1)*(z-l+1)
                            if mx>mxx:
                                mxx=mx
    print(mxx)
            
    
    
    