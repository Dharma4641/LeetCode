class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res=[]
        for i in range(len(expression)):
            oper=expression[i]
            if oper=='+' or oper=='-' or oper=='*':
                str1=expression[:i]
                str2=expression[i+1:]
                n1=self.diffWaysToCompute(str1)
                n2=self.diffWaysToCompute(str2)
                for i in n1:
                    for j in n2:
                        if oper=='+':
                            res.append(int(i)+int(j))
                        elif oper=='-':
                            res.append(int(i)-int(j))
                        elif oper=='*':
                            res.append(int(i)*int(j))
        if len(res)==0:
            res.append(int(expression))

        return res
