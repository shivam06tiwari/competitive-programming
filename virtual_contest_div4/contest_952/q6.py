from sys import stdin
input=lambda :stdin.readline()[:-1]
 
def solve():
  k,n=map(int,input().split())
  a=list(map(int,input().split()))
  c=list(map(int,input().split()))
  
  
  def calc(mid):
    res=0
    for i in range(n):
      res+=((mid+c[i]-1)//c[i])*a[i]
    return res>=k
  
  ok,ng=10**12,-1
  while ok-ng>1:
    mid=(ng+ok)//2
    if calc(mid):
      ok=mid
    else:
      ng=mid
  print(ok)
 
 
 
for _ in range(int(input())):
  solve()