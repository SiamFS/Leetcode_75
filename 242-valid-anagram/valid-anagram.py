class Solution(object):
    def isAnagram(self, s, t):
        if len(s)==len(t):
           return sorted(s)==sorted(t)
        return False
        