class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        mini=float("inf")
        while(left<=right):
            med=(right+left)//2
            sum=0
            for i in piles:
               sum+=math.ceil(i/med)
            if sum<=h:
                mini=min(med,mini)
                right=med-1
            elif sum>h:
                left=med+1
            else:
                right=med-1    
        return mini       
