class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        my_list=[]
        for q in queries:
          mini=float('inf')  
          for r in intervals:
            first=r[0]
            second=r[1]
            if first <= q <= second:
               length=second-first+1
               mini=min(length,mini)   
          if mini == float("inf"):
            my_list.append(-1)
          else: 
            my_list.append(mini) 
        return  my_list       