class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in p:
                return(i,p[d])
            else:
                p[nums[i]] = i