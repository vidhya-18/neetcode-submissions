class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dist1={i: 0 for i in range(26)}
        my_dist2={i: 0 for i in range(26)}
        for i in s:
            index= ord(i) - ord('a')
            my_dist1[index]+=1
        for j in t:
            index= ord(j) - ord('a')
            my_dist2[index]+=1    
        for i in range(0,26):
            if my_dist1[i]!=my_dist2[i]:
             return False
        return True         

          