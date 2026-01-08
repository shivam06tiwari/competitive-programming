for _ in range(int(input())):
    a,b,c = map(int,input().split())
    ca = 0
    cb = 0
    if c%2 != 0:
        ca = a + c//2 +1
        cb = b + c//2
    else:
        ca = a + c//2
        cb = b + c//2
    if ca <= cb:
        print("SECOND")
    else:
        print("FIRST")
        