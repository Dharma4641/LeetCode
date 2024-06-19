class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dict1={1:['q','Q','w','W','e','E','r','R','t','T','y','Y','u','U','i','I','o','O','p','P'],
               2:['a','A','s','S','d','D','f','F','g','G','h','H','j','J','k','K','l','L'],
               3:['z','Z','x','X','c','C','v','V','b','B','n','N','m','M']
        }
        s1=0
        s2=0
        s3=0
        res=[]
        for i in words:
            for j in i:
                if j in dict1[1]:
                    s1+=1
                if j in dict1[2]:
                    s2+=1
                if j in dict1[3]:
                    s3+=1
            if s1==len(i) or s2==len(i) or s3==len(i):
                res.append(i)
            s1=s2=s3=0
        return res