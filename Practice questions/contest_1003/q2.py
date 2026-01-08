for _ in range(int(input())):
    a = list(input())
    flag = 0
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            print(1)
            flag = 1
            break
    if flag == 0:
        print(len(a))