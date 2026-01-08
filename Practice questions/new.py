answer = []
t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    if a>=b:
        answer.append(a)
    else:
        while not(a>=b):
            a -= 1
            b -= 2
            if a==0:
                break
        answer.append(a)
for ans in answer:
    print(ans)