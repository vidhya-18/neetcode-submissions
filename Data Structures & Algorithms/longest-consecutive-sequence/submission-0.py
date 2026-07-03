class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt=0
        longest=1
        n=len(nums)
        if n==0:
            return 0
        nums.sort()
        last=float('-inf') 

        for i in range(n):
            if nums[i]-1==last:
                cnt+=1
                last=nums[i]
            elif nums[i] != last:
                cnt=1
                last=nums[i]    
            longest=max(longest,cnt)    
        return longest    
