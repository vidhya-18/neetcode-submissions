class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
         return False 
        left=0
        k=len(s1)
        need={}
        have={}
        for i in s1:
            need[i]=need.get(i,0)+1
        for right in range(len(s2)):
            have[s2[right]]=have.get(s2[right],0)+1
            if (right-left+1) >k:
                have[s2[left]]-=1
                if have[s2[left]]==0:
                    del have[s2[left]]
                left+=1    
            if need==have:
                return True  
        return False              
                  
