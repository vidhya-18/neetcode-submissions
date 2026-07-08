class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi=0
        left,right=0,len(heights)-1
        while(left<right):
            length=min(heights[left],heights[right])
            breadth=right-left
            res=length*breadth
            maxi=max(maxi,res)
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1    
        return maxi        