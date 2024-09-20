class Solution:

    def shortestPalindrome(self, s: str) -> str:
        def find(s,s1):
            stri=s+'#'+s1
            i=1
            k=0
            li=[0]*len(stri)
            while(i<len(stri)):
                if stri[i]==stri[k]:
                    k+=1
                    li[i]=k
                    i+=1
                else:
                    if k>0:
                        k=li[k-1]
                    else:
                        li[i]=0
                        i+=1
            return li[-1]
        count=find(s,s[::-1])
        return s[count:][::-1]+s


        