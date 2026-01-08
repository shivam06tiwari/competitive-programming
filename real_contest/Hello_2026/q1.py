for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if (a[0] == 1 or a[-1] == 1):
        print("ALICE")
    else:
        print("BOB")