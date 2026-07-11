class Solution(object):
    def containsDuplicate(self, nums):
         dic={}
         flag=False
         for i in nums:
            if i not in dic:
                dic[i]=1
            else: 
                flag=True
                return flag
         return flag        