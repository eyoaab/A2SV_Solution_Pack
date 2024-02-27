class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for i in s:
            if i==']':
                temp=[]
                while stack[-1]!='[':
                    temp.append(stack.pop())
               
                stack.pop()
                num=[]
                while stack and  (not stack[-1].isalpha()) and stack[-1] not in "[":
                    num.append(stack.pop()) 
                num=num[::-1]
                print(num)
               
                temp=temp[::-1]
                # print(num)
                n="".join(num)
                n=int(n)
                temp=list(n*(''.join(temp)))
                stack.extend(temp)
            else:
                stack.append(i)

        return ''.join(stack)        


        