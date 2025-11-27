class Solution(object):
    def reverseVowels(self, s):
        v="aeiouAEIOU"
        word=list(s)
        start=0
        end=len(s)-1
        while start<end:
            while start<end and word[start] not in v:
                start+=1
            while start<end and word[end] not in v:
                end-=1
            word[start],word[end]=word[end],word[start]
            start+=1
            end-=1
        return "".join(word)