import sys
from collections import Counter
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0
    d = Counter(a)
    mx = d.most_common(1)[0][1]
    c += n-mx
    while mx < n:
        mx *= 2
        c += 1
    print(c)
