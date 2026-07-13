class Solution:
    def findMin(self, nums: List[int]) -> int:
         left,right=0,len(nums)-1
         mini=float("inf")
         while(left<=right):
            med=(right+left)//2
            if(nums[left]<=nums[right]):
                mini=min(nums[left],mini)
                break
            elif(nums[left]<=nums[med]):
                mini=min(nums[left],mini)
                left=med+1
            else:
                mini=min(nums[med],mini)
                right=med-1
         return mini                   
