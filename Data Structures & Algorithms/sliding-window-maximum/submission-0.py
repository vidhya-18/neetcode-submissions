class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        count=0
        left,right=0,0
        my_list=[]
        max_list=[]
        while right<len(nums):
            if count<k:
                my_list.append(nums[right])
                count+=1
                right+=1

            else:
                max_list.append(max(my_list))
                del my_list
                my_list=[]
                right=left+1
                left+=1
                count=0
        if count == k:
         max_list.append(max(my_list))
        return max_list
