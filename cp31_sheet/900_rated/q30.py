for _ in range(int(input())):
    s = input()
    m = 0
    while len(s) != 0 and s.count("1") != len(s) and s.count("0") != len(s):
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                m += 1
                s = s[:i] + s[i+2:]
                break
    if m%2 == 0:
        print("NET")
    else:
        print("DA")