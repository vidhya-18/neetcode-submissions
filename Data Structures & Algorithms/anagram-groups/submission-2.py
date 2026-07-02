class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            count=[0]*26
            for i in word:
                count[ord(i)-ord('a')]+=1
            key=tuple(count)
            if key not in d:
              d[key]=[]
            d[key].append(word)
        return list(d.values())    
