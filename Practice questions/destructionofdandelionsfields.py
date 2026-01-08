L = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    even_sum = 0
    ans = 0
    odd = []
    for ch in a:
        if ch%2 == 0:
            even_sum += ch
        else:
            odd.append(ch)
    odd.sort()
    if len(odd) == 0:
        ans = 0
    else:
        ans += even_sum
        if (len(odd))%2 == 0:
            for i in range((len(odd))//2):
                ans += odd[-i-1]
        else:
            for i in range((len(odd)//2)+1):
                ans += odd[-i-1]
    L.append(ans)
for ch in L:
    print(ch)
            
            
                
    