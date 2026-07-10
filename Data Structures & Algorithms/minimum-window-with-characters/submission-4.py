class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) :
            return ""
        need={}  
        for i in t:
            need[i]=need.get(i,0)+1
        needcount=len(need)
        havecount=0
        reslen=float("inf")   
        res=[-1,-1] 
        left=0
        have={}
        for right in range(len(s)):
            have[s[right]]=have.get(s[right],0)+1
            c=s[right]
            if c in need and have[c]==need[c]:
                havecount+=1
                while havecount==needcount:
                    if (right-left+1)<reslen:
                        res=[left,right]
                        reslen=right-left+1
                    have[s[left]]-=1
                    if s[left] in need and have[s[left]] < need[s[left]]:
                        havecount-=1
                    left+=1        
        l,r=res
        return s[l:r+1] if reslen != float("inf") else ""