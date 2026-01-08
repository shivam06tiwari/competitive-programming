n = int(input())
Solution = []
for i in range(n):
    tries = 0
    a, b = map(int, input().split())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    while L != []:
        if len(L) >= b:
            x = L[b-1]
            for j in range(b):
                L[j] -= x
            tries += x
        else:
            x = L[-1]
            for j in range(len(L)):
                L[j] -= x
            tries += x
        L = [item for item in L if item > 0]
        L.sort(reverse=True)
    Solution.append(tries)
for num in Solution:
    print(int(num))
                
        
        