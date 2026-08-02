class Solution(object):

    def reverse(self, x):

      
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)

        result = 0

        while x > 0:

            digit = x % 10

            result = result * 10 + digit

            x = x // 10


        result = result * sign

        if result < -2147483648:
            return 0

        if result > 2147483647:
            return 0

        return result
        