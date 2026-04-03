class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for str in strs: 
            s = tuple(sorted(str))
            if s not in groups:
                groups[s] = []
            groups[s].append(str)

        ans = []

        for s in groups:
            ans.append(groups[s])

        return ans