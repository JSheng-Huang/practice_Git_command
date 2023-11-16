"""Minimum Partition
Problem:
        Given a set of integers, the task is to divide it into two sets S1 and 
    S2 such that the absolute difference between their sums is minimum. 
        If there is a set S with n elements, then if we assume Subset1 has m 
    elements, Subset2 must have `n - m` elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.
Example:
    Input:  arr[] = {1, 6, 11, 5} 
    Output: 1
    Explanation:
        Subset1 = {1, 5, 6}, sum of Subset1 = 12 
        Subset2 = {11}, sum of Subset2 = 11    
Refer to:
    1. https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
    Time Complexity: O(n * sum), where `n` is the number of elements and `sum` 
    is the sum of all elements.
    Space Complexity: O(sum)
Created by JSheng <jasonhuang0124@gmail.com>"""


def minDifference(arr, n):
    sum = 0
    for i in range(n):
        sum += arr[i]
    """
    The half of sum of two subsets would be the closet one to the difference of 
    two subsets.
    """
    y = sum // 2 + 1
    print('y:', y)
    # dp[i] gives whether is it possible to get i as
    # sum of elements dd is helper variable we use dd
    # to ignoring duplicates
    dp = [False for i in range(y)]
    dd = [False for i in range(y)]

    # Initializing dp and dd

    # sum = 0 is possible
    dp[0] = True
    # let dp array is used for storing
    # previous values and dd array is used to
    # store current values
    for i in range(n):

        # updating dd[k] as True if k can be formed
        # using elements from 1 to i+1
        for j in range(y):
            if j + arr[i] < y and dp[j]:
                dd[j + arr[i]] = True
        print('dd:', dd)
        print('...')
        # updating dd
        for j in range(y):
            if (dd[j]):
                dp[j] = True
            dd[j] = False  # reset dd
        print('dp:', dp)
        print('---')
    # checking the number from sum/2 to 1 which is
    # possible to get as sum
    for i in range(y - 1, 0, -1):
        if (dp[i]):
            print('dp:', dp)
            print('sum:', sum)
            print('i:', i)
            return (sum - 2 * i)

        # since i is possible to form then another
        # number is sum-i so min difference is sum-i-i
    return 0


if __name__ == '__main__':
    arr = [1, 5, 5, 11, 16]
    n = len(arr)
    print("The Minimum difference of 2 sets is ", minDifference(arr, n))
