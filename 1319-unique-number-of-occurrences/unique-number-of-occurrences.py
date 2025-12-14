class Solution(object):
    def uniqueOccurrences(self, arr):
        dic={}
        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        lst=set()
        for i in dic.values():
            if i in lst:
               return False
            lst.add(i)
        return True 
        