class Solution(object):
    def isPowerOfFour(self, n):
        def rec(n):
            if n==0:
                return False
            if n==1:
                return True
            if n%4==0:
                return rec(n//4)
            return False
        return rec(n)
        