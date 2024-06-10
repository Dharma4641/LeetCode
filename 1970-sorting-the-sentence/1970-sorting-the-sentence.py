class Solution(object):
    def sortSentence(self, s):
        b=s.split(" ")
        li=[0]*len(b)
        print(b)
        for i in range(len(b)):
             li[int(b[i][-1])-1]=b[i][:-1]
        return ' '.join(li)
