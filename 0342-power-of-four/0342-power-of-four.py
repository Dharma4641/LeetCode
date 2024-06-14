class Solution(object):
    def isPowerOfFour(self, n):
        def rec(n):
            if n==0:
                return False
            elif n==1:
                return True
            else:
                return  n%4==0  and rec(n//4)
        return rec(n)
        