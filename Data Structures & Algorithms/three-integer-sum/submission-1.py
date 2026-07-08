class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st=set()
        for i in range(len(nums)):
            my_list=set()
            for j in range(i+1,len(nums)):
                ser= -(nums[i]+nums[j])
                if ser in my_list:
                   ele=tuple(sorted([nums[i],nums[j],ser]))
                   st.add(ele)
                my_list.add(nums[j])
                
        return [list(ele) for ele in st]                