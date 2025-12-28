class Solution(object):
    def lengthOfLastWord(self, s):
        lst=s.split()

        return len(lst[-1])
        