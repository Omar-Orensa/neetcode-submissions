class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []
        for n in nums:
            count[n] += 1
        result = [num for num, freq in sorted(count.items(), key=lambda item: item[1], reverse=True)[:k]]
        return result

