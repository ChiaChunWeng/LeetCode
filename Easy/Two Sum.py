"""
    Given an array of integers nums and an integer target,

    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Best Solution:
        class Solution:
            def twoSum(self, nums, target):
                h = {}
                for i, num in enumerate(nums):
                    n = target - num
                    if n not in h:
                        h[num] = i
                    else:
                        return [h[n], i]

    https://leetcode.com/problems/two-sum

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    input = [2, 7, 11, 15]
    target = 9
    Result = Solution().twoSum(nums=input, target=target)
    print(Result)
