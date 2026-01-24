d = map(int,open(0,'rb').read().split())
t = next(d)
for _ in range(t):
    n,k = next(d),next(d)
    l = []
    for i in range(n):
        p = []
        for j in range(n):
            p.append(next(d))
        l.append(p)
    c = 0
    for i in range((n+1)//2):
        for j in range(n):
            if l[i][j] != l[n-i-1][n-j-1]:
                if i == n-i-1:
                    c += 0.5
                else:
                    c += 1
        if c>k:
            print("NO")
            break
    else:
        c = int(c)
        if n%2 == 1:
            print("YES")
        else:
            if (k-c)%2 == 0:
                print("YES")
            else:
                print("NO")
                
# method 2

import sys, os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    c = 0
    for i in range((n+1)//2):
        for j in range(n):
            if l[i][j] != l[n-i-1][n-j-1]:
                if i == n-i-1:
                    c += 0.5
                else:
                    c += 1
        if c>k:
            sys.stdout.write("NO\n")
            break
    else:
        c = int(c)
        if n%2 == 1:
            sys.stdout.write("YES\n")
        else:
            if (k-c)%2 == 0:
                sys.stdout.write("YES\n")
            else:
                sys.stdout.write("NO\n")
                
                
# method 3

import sys
d = iter(map(int, sys.stdin.read().split()))
t = next(d)
for _ in range(t):
    n, k = next(d), next(d)
    l = []
    for i in range(n):
        p = []
        for j in range(n):
            p.append(next(d))
        l.append(p)
    c = 0
    for i in range((n+1)//2):
        for j in range(n):
            if l[i][j] != l[n-i-1][n-j-1]:
                if i == n-i-1:
                    c += 0.5
                else:
                    c += 1
        if c>k:
            sys.stdout.write("NO\n")
            break
    else:
        c = int(c)
        if n%2 == 1:
            sys.stdout.write("YES\n")
        else:
            if (k-c)%2 == 0:
                sys.stdout.write("YES\n")
            else:
                sys.stdout.write("NO\n")
                
# method 4

import sys, os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    c = 0
    for i in range((n+1)//2):
        for j in range(n):
            if l[i][j] != l[n-i-1][n-j-1]:
                if i == n-i-1:
                    c += 0.5
                else:
                    c += 1
        if c>k:
            print("NO")
            break
    else:
        c = int(c)
        if n%2 == 1:
            print("YES")
        else:
            if (k-c)%2 == 0:
                print("YES")
            else:
                print("NO")