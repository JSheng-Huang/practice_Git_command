"""LeetCode#1862(Hard) Sum of Floored Pairs
Link: https://leetcode.com/problems/sum-of-floored-pairs/
Problem:
        Given an integer array nums, return the sum of floor(nums[i] / nums[j]) 
    for all pairs of indices 0 <= i, j < nums.length in the array. Since the 
    answer may be too large, return it modulo `10 ** 9 + 7`.
        The floor() function returns the integer part of the division.
Note: N/A.
Example:
    #1:
      Input: nums = [2,5,9]
      Output: 10
      Explanation:
            floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
            floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 3
            floor(5 / 2) = 2
            floor(9 / 2) = 4
            floor(9 / 5) = 1
            We calculate the floor of the division for every pair of indices in 
        the array then sum them up.
    #2:
      Input: nums = [7,7,7,7,7,7,7]
      Output: 49
Constraints: 
    #1. 1 <= nums.length <= 105
    #2. 1 <= nums[i] <= 105
Refer to: 
    Time Complexity: ???
    Space Complexity: ???
    Explanation: ???
Date: 231215.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    res += (nums[i] // nums[j])
                else:
                    res += (nums[j] // nums[i])
        return res + len(nums) - 1


if __name__ == '__main__':
    qwe = Solution()

    """Return `10`."""
    print(qwe.sumOfFlooredPairs([2, 5, 9]))

    """Return `49`."""
    # print(qwe.sumOfFlooredPairs([7,7,7,7,7,7,7]))
