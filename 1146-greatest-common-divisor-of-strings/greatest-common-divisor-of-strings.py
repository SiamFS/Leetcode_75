class Solution(object):
    def gcdOfStrings(self, str1, str2):
        
        # Check if gcd string is even possible
        if str1 + str2 != str2 + str1:
            return ""
        
        len1 = len(str1)
        len2 = len(str2)
        
        # Euclid GCD
        while len2 != 0:
            rem = len1 % len2
            len1 = len2
            len2 = rem
        
        # len1 is now gcd length
        return str1[:len1]
