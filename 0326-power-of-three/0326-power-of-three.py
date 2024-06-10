import math
class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        res=math.log10(n)/math.log10(3)
        return res.is_integer()
            
        