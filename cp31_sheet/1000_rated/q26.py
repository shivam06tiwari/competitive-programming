for _ in range(int(input())):
    x,y,k = map(int,input().split())
    z = (((y+1)*k)-3+x)//(x-1)
    print(z+k)