class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        memo = {}

        def dp(pos):
            if pos in memo:
                return memo[pos]
            
            res = 1;
            for j in range(pos + 1, n):
                if intervals[pos][1] <= intervals[j][0]:
                    res = max(res, 1 + dp(j))
            
            memo[pos] = res
            return res

        return n - dp(0)


        