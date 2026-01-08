for _ in range(int(input())):
    n,a,b= map(int,input().split())
    if n == a and a == b:
        print("Yes")
    elif a+b+2 <= n:
        print("Yes")
    else:
        print("No")