class Solution:
    def rev(self,x):
     num=0
     while(x>0):
        num=num*10 + x%10
        x//=10
     return num   
    def reverse(self, x: int) -> int:
        if x<0:
            x=x*-1
            x=self.rev(x)
            if(x>=2**31-1):
                return 0
            return x*-1

        else:
            x=self.rev(x)
            if(x>=2**31-1):
                return 0
            return x        
        