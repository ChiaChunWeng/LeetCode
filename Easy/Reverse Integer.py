"""
    Given a 32-bit signed integer, reverse digits of an integer.

    Note:

    Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1].

    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        reverse_number = 0
        if x > 0:
            print("Positive")
            while x > 0:
                remainder = x % 10
                reverse_number = (reverse_number * 10) + remainder
                x = x // 10
            print(reverse_number)

        else:
            print("negative")
            x = x * (-1)
            while x > 0:
                remainder = x % 10
                reverse_number = (reverse_number * 10) + remainder
                x = x // 10
            reverse_number = reverse_number * (-1)
        if -2147483648 < reverse_number < 2147483647:
            return reverse_number
        else:
            return 0


if __name__ == '__main__':
    input = 1534236469
    Solution().reverse(input)
