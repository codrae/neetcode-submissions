from collections import Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        c = Counter(nums)
        if c[0] > 1 :
            return [0] * len(nums)
        
        all_product = 1
        for num in nums:
            if num == 0:
                continue
            all_product *= num
        
        for i,num in enumerate(nums):
            if num == 0:
                ans[i] = all_product
                return [0] * i + [all_product] + [0] * (len(nums)-i-1)
            else:
                ans[i] = all_product // num
        
        return ans
