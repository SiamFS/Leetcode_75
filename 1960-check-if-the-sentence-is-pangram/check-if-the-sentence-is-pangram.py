class Solution(object):
    def checkIfPangram(self, sentence):
         table=[False]*26
         for i in sentence:
            if "a"<=i.lower()<="z":
                table[ord(i.lower())-ord("a")]=True
         for i in table:
            if not i:
                return False
         return True


