class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for num in nums:
           d[num]=d.get(num,0)+1
        sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)        
        K=1
        for i in sorted_items:
          if K <=k:  
           l.append(i[0])
           K+=1
        return l   