class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = bytearray(26)
            for c in s:
                count[ord(c) - 97] += 1
            res[bytes(count)].append(s)
        return list(res.values())