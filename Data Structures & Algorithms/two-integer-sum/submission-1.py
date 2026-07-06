class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for i, x in enumerate(nums):
            dif = target - x
            if dif not in seen:
                seen[x] = i
            else:
                res = [seen[dif], i]
                return res
        return res