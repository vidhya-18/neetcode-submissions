class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt=0
        intervals.sort(key=lambda x: x[0])
        my_list=intervals[0][1]
        for i in range(1,len(intervals)):
            if my_list > intervals[i][0]:
                cnt+=1
                my_list=min(my_list,intervals[i][1])
            else:
                my_list=intervals[i][1]
                
        return cnt                 