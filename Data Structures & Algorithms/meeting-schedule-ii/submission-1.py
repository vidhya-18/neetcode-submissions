"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start=sorted(i.start for i in intervals)
        end=sorted(i.end for i in intervals)
        room=0
        max_room=0
        s=0
        e=0
        while(s<len(intervals)):
            if start[s] < end[e]:
                room+=1
                s+=1
                max_room=max(room,max_room)
            else:
                e+=1
                room-=1     
        
        return max_room        