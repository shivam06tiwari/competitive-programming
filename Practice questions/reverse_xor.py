for _ in range(int(input())):
    n = int(input())
    b = list(bin(n)[2:])
    flag = 0
    while b[-1] == "0" and b != ["0"]:
        b.pop(-1)
    if b == ["1"]:
        flag = 1
    elif b == ["0"]:
        flag = 0
    else:
        k = len(b)
        for i in range(k//2):
            if b[i] == b[k-i-1]:
                flag = 0
            else:
                flag = 1
                break
        if flag == 0:
            if k%2 != 0:
                if b[(k//2)] == "0":
                    flag = 0
                else:
                    flag = 1
    if flag == 1:
        print("NO")
    else:
        print("YES")
        
            
        