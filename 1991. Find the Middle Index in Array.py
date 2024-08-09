class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        n = 0
    
        for i, num in enumerate(nums):
            total-= num
            if n == total:
                return i
            n += num
    
        return -1
