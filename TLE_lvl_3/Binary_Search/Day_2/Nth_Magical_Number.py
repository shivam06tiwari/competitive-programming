import math
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l = 1
        mn = min(a,b)
        mx = max(a,b)
        h = mn*n
        ans = -1
        while l<=h:
            c = 0
            m = l + (h-l)//2
            c += m//mx + m//mn
            c -= m//math.lcm(mn,mx)
            if c >= n:
                ans = m%(10**9+7)
                h = m-1
            else:
                l = m+1
        return(ans)