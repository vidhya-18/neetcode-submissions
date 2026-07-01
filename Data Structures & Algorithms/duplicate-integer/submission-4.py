class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_list=[]
        for i in nums:
            if i in my_list:
                return True
            else:
                my_list.append(i)
        return False                   
        