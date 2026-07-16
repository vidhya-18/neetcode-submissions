class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        n=len(nums1)
        m=len(nums2)
        left,right=0,n 
        while(left<=right):
            part1=(left+right)//2
            part2=(m+n+1)//2-part1
            left1=float("-inf") if part1==0 else nums1[part1-1]
            right1=float("inf") if part1==n else nums1[part1]
            left2=float("-inf") if part2==0 else nums2[part2-1]
            right2=float("inf") if part2==m else nums2[part2]  
            if(left1<=right2 and left2<=right1):
                if(n+m)%2==0:
                    return (max(left1,left2)+min(right1,right2))/2 
                else:
                    return max(left1,left2)    
            elif(left1>right2):
                right=part1-1
            else:
                left=part1+1
                             
