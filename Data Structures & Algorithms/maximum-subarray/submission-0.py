class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        max_sum=-1
        for i in nums:
            sum+=i
            if sum<0:
                sum=0
            else:
                max_sum=max(max_sum,sum)
        return max_sum            