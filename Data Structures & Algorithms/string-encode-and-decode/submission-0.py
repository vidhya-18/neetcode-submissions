class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i))+"$"+i
        return res    

    def decode(self, s: str) -> List[str]:
        i=0
        decoded=[]
        while i < len(s):
            j=s.find("$",i)
            length=int(s[i:j])
            decoded.append(s[j+1:j+length+1])
            i=j+length+1
        return decoded    
