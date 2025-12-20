class Solution(object):
    def maxVowels(self, s, k):
         left=0
         right=k
         v="aeiouAEIOU"
         count=0
         temp=0
         for i in range(k):
            if s[i] in v:
                temp+=1
         count=temp
         for i in range(k,len(s)):
             if s[i] in v:
                temp+=1
             if s[i-k] in v:
                temp-=1
             count=max(count,temp)
         return count

         
        