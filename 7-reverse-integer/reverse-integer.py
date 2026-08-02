class Solution(object):

    def reverse(self, x):

        # Store the original sign
        if x < 0:
            sign = -1
        else:
            sign = 1

        # Convert the number to a positive value
        x = abs(x)

        result = 0

        while x > 0:

            digit = x % 10

            result = result * 10 + digit

            x = x // 10

        # Restore the sign
        result = result * sign

        # Check the lower limit
        if result < -2147483648:
            return 0

        # Check the upper limit
        if result > 2147483647:
            return 0

        return result
        