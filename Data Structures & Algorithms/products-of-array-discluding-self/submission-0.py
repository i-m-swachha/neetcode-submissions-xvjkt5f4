class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) - 1
        res = 1;
        zero = 0
        for i in nums:
            if i == 0:
                zero += 1
                continue
            res *= i
        

        ans = []

        for i in nums:
            if zero > 1:
                ans.append(0)
                continue;
            if i == 0:
                ans.append(res)
                continue
            if zero:
                ans.append(0)
            else:
                ans.append(int(res / i))
        
        return ans