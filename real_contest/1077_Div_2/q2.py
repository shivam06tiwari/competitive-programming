for _ in range(int(input())):
    n = int(input())
    s = list(input())
    if n == 1:
        print(1)
    else:
        for i in range(n):
            if s[i] == "1":
                if i == 0 and n>1:
                    s[i+1] = "2"
                elif i == n-1 and n>1:
                    s[i-1] = "2"
                else:
                    s[i-1] = "2"
                    s[i+1] = "2"
        c = 0
        ans = 0
        for i in range(n):
            if s[i] == "0":
                c += 1
            else:
                ans += (c+2)//3
                c = 0
        if c != 0:
            ans += (c+2)//3
        print(ans+s.count("1"))
    