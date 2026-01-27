class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Binary Search Method
        l = 1
        r = len(nums)-1
        ans = 0
        while l<=r:
            c = 0
            m = l + (r-l)//2
            for ch in nums:
                if ch <= m:
                    c += 1
            if c >= m+1:
                ans = m
                r = m-1
            else:
                l = m+1
        return(ans)