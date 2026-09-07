class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = dict()
        res = []
        for w in strs:
            key = tuple(sorted(w))
            temp.setdefault(key, []).append(w)

        for v in temp.values():
            res.append(v)
        return res
