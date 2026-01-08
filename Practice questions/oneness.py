t = int(input())
answer = []
for _ in range(t):
    z = int(input())
    a = str(0)
    b = str(1)
    if z%2==0:
        answer.append((int(z/2))*a + (int(z/2))*b)
    elif z == 1:
        answer.append(0)
    else:
        answer.append((int((z-1)/2))*b + (int((z+1)/2))*a)
for ans in answer:
    print(ans)

        

        