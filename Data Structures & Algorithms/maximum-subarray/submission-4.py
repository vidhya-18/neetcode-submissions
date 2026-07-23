class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        max_sum=nums[0]
        for i in nums:
            if sum<0:
                sum=0
            sum+=i    
            if max_sum<sum:
                max_sum=sum
        return max_sum            