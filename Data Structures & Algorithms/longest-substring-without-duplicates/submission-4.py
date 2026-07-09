class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        left,right=0,1
        my_list=[s[0]]
        maxcount=1
        while(right<len(s)):
            while s[right] in my_list:
                my_list.remove(s[left])
                left+=1
            my_list.append(s[right])
            maxcount=max(maxcount,len(my_list))    
            right+=1
        return maxcount     