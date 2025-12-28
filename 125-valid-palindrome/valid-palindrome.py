class Solution(object):
    def isPalindrome(self, s):
        F=False
        new=""
        for i in s:
            if i.isalnum():
                new +=i.lower()
        if new==new[::-1]:
            F=True
        return F
        