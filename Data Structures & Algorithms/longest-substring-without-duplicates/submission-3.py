class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        left,right=0,1
        count=1
        maxcount=1
        my_list=[]
        while(right<len(s)):
            if s[left]==s[right]:
                left+=1
            elif s[left]!=s[right] and s[right] not in my_list:
                count+=1
                my_list.append(s[right])
                maxcount=max(maxcount,count)
            else:
                left=right
                count=1 
                my_list=[]   
            right+=1
            
        return maxcount     