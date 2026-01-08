t = int(input(""))
answer = []
for _ in range(t):
    score = 0
    z = int(input())
    l = list(map(int,input().split()))

    if z!= 1:
        l.sort()
        min = l[0]
        max = l[-1]
        score += max - min
        l.remove(max)
        
        for j in l[1:]:
           if j < min:
               min = j
           score += max- min
    answer.append(score)
for ans in answer:
    print(ans)
    
    