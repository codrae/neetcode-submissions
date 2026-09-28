class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # 값 -> 인덱스
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i