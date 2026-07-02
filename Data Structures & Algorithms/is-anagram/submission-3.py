class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if(len(s) != len(t)):
            return False
        for i in s:
            count[i] = count.get(i, 0) + 1
        for m in t:
            count[m] = count.get(m, 0) - 1
        for k, v in count.items():
            if v != 0:
                return False
        return True
        