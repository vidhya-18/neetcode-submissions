class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        my_list=[]
        n=len(nums)
        for i in range(n):
            prod=1
            for j in range(n):
                if i!=j:
                   prod*= nums[j] 
            my_list.append(prod) 
        return my_list         