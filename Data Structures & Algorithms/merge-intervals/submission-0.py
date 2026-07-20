class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        my_list=[intervals[0]]
        for i in range(1,len(intervals)):
          if(my_list[-1][1]>=intervals[i][0]):
            my_list[-1][0]=min(my_list[-1][0],intervals[i][0])
            my_list[-1][1]=max(my_list[-1][1],intervals[i][1])
          else:
            my_list.append(intervals[i])
        return my_list      