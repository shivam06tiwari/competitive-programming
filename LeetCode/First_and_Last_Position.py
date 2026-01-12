class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return([-1,-1])
        k = -2
        ans = []
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                k = mid
                while k>0 and nums[k-1] == target:
                    k -= 1
                ans.append(k)
                k = mid
                while k<len(nums)-1 and nums[k+1] == target:
                    k += 1
                ans.append(k)
                return(ans)
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if k == -2:
            return([-1,-1])