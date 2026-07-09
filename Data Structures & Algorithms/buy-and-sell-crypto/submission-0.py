class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        n=len(prices)
        leftmin=[0]*n
        rightmax=[0]*n
        leftmin[0]=prices[0]
        rightmax[n-1]=prices[n-1]
        for i in range(1,n):
            leftmin[i]=min(prices[i],leftmin[i-1])
        for i in range(n-2,-1,-1):
            rightmax[i]=max(prices[i],leftmin[i+1])  
        for i in range(n):
            res=rightmax[i]-leftmin[i]
            maxi=max(maxi,res)    
        return maxi  