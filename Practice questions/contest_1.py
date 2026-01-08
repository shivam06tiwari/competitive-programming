n = int(input())
Solution = []
for i in range(n):
    happy = 0
    buffer = 0
    L=[]
    a,b = map(int,input().split())
    m = input()
    m = m.split()
    for ch in m:
        L.append(int(ch))
    for x in L:  
        if x%2 == 0:
            happy += x
            b -= x/2
        else:
            happy += x - 1
            buffer += 1
            b -= (x-1)/2
    if buffer - b > 0:
        happy += 2*b-buffer
    else:
        happy += buffer
    Solution.append(happy)
for num in Solution:
    print(int(num))
        
            
        
            
        
        
