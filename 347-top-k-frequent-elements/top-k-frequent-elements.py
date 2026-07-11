class Solution(object):
    def topKFrequent(self, nums, k):
         dic={}
         frq=[[] for i in range(len(nums)+1)]
         for i in nums:
            dic[i]=dic.get(i,0)+1
         for key,values in dic.items():
             frq[values].append(key)
         lst=[]
         for i in range(len(frq)-1,0,-1):
             for j in frq[i]:
                lst.append(j)
                if len(lst)==k:
                    return lst
         return lst