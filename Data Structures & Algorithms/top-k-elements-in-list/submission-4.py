class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        buckets = [[] for _ in range(len(nums)+1)]

        for num in nums:
            count_map[num] = count_map.get(num,0) + 1
        for num , count in count_map.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
            if len(res) == k:
                return res
        