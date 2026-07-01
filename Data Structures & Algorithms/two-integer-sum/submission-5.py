class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_list=[(num,idx) for idx,num in enumerate(nums)]
        my_list.sort(key=lambda x:x[0])
        left,right=0,len(nums)-1
        while(left<right):
           sum=my_list[left][0]+my_list[right][0] 
           if(sum==target):
             return sorted([my_list[left][1],my_list[right][1]])
           elif(sum>target):
             right-=1
           else:
            left+=1           

        return [-1,-1]          