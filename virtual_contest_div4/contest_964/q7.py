for _ in range(int(input())):
    low = 2
    high = 999
    while high > low:
        m1 = low + (high -low)//3
        m2 = low + 2*(high -low)//3
        print("?",m1,m2,flush=True)
        x = int(input())
        if x == m1*m2:
            low = m2+1
        elif x == m1*(m2+1):
            low = m1+1
            high = m2
        else:
            high = m1
    print("!",low)