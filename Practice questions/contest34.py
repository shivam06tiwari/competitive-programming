t=int(input())
results=[]
for _ in range(t):
    n,k=map(int,input().split())
    num=list(map(int,input().split()))
    num.sort()
    unique_cards=set()
    count=0
    for card in num:
        if card not in unique_cards:
            if len(unique_cards)>=k:
                break
            unique_cards.add(card)
        count+=1
    results.append(count)
for res in results:
    print(res)

