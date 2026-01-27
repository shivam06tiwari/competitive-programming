class Solution:
    def minDays(self, a: list[int], o: int, k: int) -> int:
        l = 1
        r = max(a)
        if o*k > len(a):
            return(-1)
        ans = -1
        while l<=r:
            m = l + (r-l)//2
            b = 0
            c = 0
            for ch in a:
                if ch <= m:
                    c += 1
                    if c == k:
                        c = 0
                        b += 1
                        if b >= o:
                            break
                else:
                    c = 0
            if b >= o:
                ans = m
                r = m-1
            else:
                l = m+1
        return(ans)