class Solution:
    def isPalindrome(self, s: str) -> bool:
        str="".join(i.lower() for i in s if i.isalnum())
        left,right=0,len(str)-1
        while(left<right):
            if str[left]!=str[right]:
                return False
            left+=1
            right-=1
        return True        
        