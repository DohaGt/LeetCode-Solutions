class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        p = {0: -1}
        prefix_sum = 0
    
        for i, num in enumerate(nums):
            prefix_sum += num
            r = prefix_sum % k
        
            if r in p:
                if i - p[r] > 1:
                    return True
            else:
                p[r] = i
        return False