class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in s:
            if num - 1 not in s:          # only start at the left end
                cur = num
                length = 1
                while cur + 1 in s:
                    cur += 1
                    length += 1
                res = max(res, length)
        return res