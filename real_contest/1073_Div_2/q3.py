for _ in range(int(input())):
    n = int(input())
    s = input()
    # c1 = 0
    # i1 = []
    # x = 0
    # y = []
    # for i in range(n):
    #     if s[i] == "1":
    #         c1 += 1
    #         i1.append(i)
    # m = 0
    # z = n-1
    # for i in range(c1-1,-1,-1):
    #     m += z-i1[i]
    #     z -= 1
    # if m%2 == 0:
    #     print("Bob")
    # else:
    #     if c1 == 1:
    #         x = 2
    #         y.append(i1[0]+1)
    #         y.append(i1[0]+2)
    #     else:
    #         for i in range(1,c1):
    #             if i1[i]-i1[i-1] >= 2:
    #                 x = i1[i]-i1[i-1]
    #                 y.append(i1[i-1]+1)
    #                 y.append(i1[i])
    #                 break
    #     print("Alice")
    #     print(x)
    #     print(*y)
    if list(s) == sorted(list(s)):
        print("Bob")
    else:
        i1 = []
        c1 = s.count("1")
        x = 0
        y = []
        for i in range(n-c1):
            if s[i] == "1":
                y.append(i+1)
        for i in range(n-c1,n):
            if s[i] == "0":
                y.append(i+1)
        print("Alice")
        x = len(y)
        print(x)
        print(*y)
            
        
        
    