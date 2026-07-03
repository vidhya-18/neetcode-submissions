class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest=1
        nums=set(nums)
        for num in nums:
            cur=num
            if cur-1 not in nums:
                cnt=1
                while cur+1 in nums:
                  cnt+=1
                  cur+=1
                longest=max(cnt,longest)  


    
        return longest    
