class Solution(object):
    def replaceWords(self, dictionary, sentence):
        words=sentence.split()
        s=''
        dict1=set(dictionary)
        def replace(w):
            for i in range(1,len(w)+1):
                if w[:i] in dict1:
                    return w[:i]
            return w
        replaced_words=[replace(w) for w in words]
        for i in range(len(replaced_words)-1):
            s=s+replaced_words[i]+" "
        s=s+replaced_words[i+1]
        return s


                    
        