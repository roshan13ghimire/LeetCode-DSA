class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i,num in enumerate(nums):
            out = target - num
            if out in d:
                return [d[out], i]
            d[num] = i
        return []
