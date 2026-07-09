class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)==0:
            return 0
        max_fre=0
        fre={}
        left=0
        max_len=0
        for right in range(len(s)):
            fre[s[right]]=fre.get(s[right],0)+1
            max_fre=max(max_fre,fre[s[right]])
            while(right-left+1)-max_fre>k:
                fre[s[left]]-=1
                left+=1
            max_len=max(max_len,(right-left+1))
        return max_len           