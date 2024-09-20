class Solution:
    def reverse(self, x: int) -> int:
        res=0
        if x<0:
            res= int(str(x)[1:][::-1])*-1
        elif x>0:
            res=int(str(x)[::-1])
        if res<2**31-1 and res>-2**31:
            return res
        else:
            return 0
        
        
        
        