class Solution(object):
    def isAnagram(self, s, t):
        frq={}
        for i in s:
            frq[i]=frq.get(i,0)+1
        for i in t:
            frq[i]=frq.get(i,0)-1
        for i in frq.values():
             if i !=0:
                return False
        return True