class Solution(object):
    def removeOccurrences(self, s, part):
        stack=[]
        n=len(part)
        for i in s:
            stack.append(i)
            if len(stack)>=n and "".join(stack[-n:])==part:
                for i in range(n):
                    stack.pop()
        return "".join(stack)