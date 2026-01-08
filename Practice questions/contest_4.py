p = int(input())
L = []
for i in range(p):
    cards = []
    Game = True
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    a = min(num)
    cards.append(a)
    num.remove(a)
    num.sort()
    while Game:
        for ele in num:
            if ele >= cards[-1]:
                cards.append(ele)
                num.remove(ele)
                if len(set(cards)) > k:
                    Game = False
                    break
            else:
                Game = False
        else:
            Game = False
    L.append(len(cards))
for elem in L:
    print(elem)

    
    