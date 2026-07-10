class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        my_list=[]
        max_list=[]
        for i in range(k):
            my_list.append(nums[i])
        max_list.append(max(my_list))
        for right in range(k,len(nums)):
            my_list.pop(0)
            my_list.append(nums[right])
            max_list.append(max(my_list))   
        return max_list
