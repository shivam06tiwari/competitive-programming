for _ in range(int(input())):
    n = int(input())
    s = input()
    a = 1
    ma = 0
    b = 1
    mb = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            if s[i] == ">":
                a += 1
                if a > ma:
                    ma = a
            else:
                b += 1
                if b > mb:
                    mb = b
        else:
            a = 1
            b = 1
    print(max(a,b)+1)