class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for i,num in enumerate(nums):
            rem=target-num
            if rem in my_dict:
                return [my_dict[rem],i]
            my_dict[num]=i
        return my_dict           