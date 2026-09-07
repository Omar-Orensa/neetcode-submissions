class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for word in strs:
            sortedS = ''.join(sorted(word))
            temp[sortedS].append(word)
        return(list(temp.values()))
