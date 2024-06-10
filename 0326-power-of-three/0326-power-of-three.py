class Solution(object):
    def isPowerOfThree(self, n):
        def rec(n):
            if n==1:
                return True
            if n%3==0:
                return rec(n//3)
            else:
                return False
        if n<=0:
            return False
        return rec(n)
            
        