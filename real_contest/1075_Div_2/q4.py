import sys, os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))