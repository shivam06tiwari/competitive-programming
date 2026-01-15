n = int(input())
s = input()
for i in range(n-1):
    if s[i+1]<s[i]:
        print("YES")
        break
else:
    print("NO")