# Compute the length of the longest strictly increasing subsequence in a list.
# I/P: [11, 5, 2, 5, 3, 7, 101, 18]
# O/P: 4

"""
Approach:
========
Iterate through every number in the list. 
And if the next number is strictly greater than the current num, then append to the resulting list
Else, Insert it into the list using Binary Search Insertion. 
Because, Binary search insertion will rearrange the smaller numbers in order affecting the existing longest strictly increasing subsequence
This will help us to go through the list only once and length of the resulting string will be our answer
"""

def longestStrictlyIncrSubsequence(nums):
    res = []

    def binarySearchInsertionIndex(start, end, num):
        if start > end:
            return start
        mid = (start+end)//2
        if num == res[mid]:
            return mid
        if num > res[mid]:
            return binarySearchInsertionIndex(mid+1, end, num)
        else:
            return binarySearchInsertionIndex(start, mid-1, num)

    for num in nums:
        if not res or num > res[-1]:
            res.append(num)
        elif num < res[-1]:
            index = binarySearchInsertionIndex(0, len(res), num)
            res[index] = num
    
    return len(res)

# testcases
testcases = [
    [11, 5, 2, 5, 3, 7, 101, 18],
    [],
    [1,2,2,3,4,5,6,7,1,2,3,4],
    [1,1,1,1,1,1,1],
    [2,5,10,5,3,4,9],
    [7,6,5,4,3,2,1,1],
]

for testcase in testcases:
    print(longestStrictlyIncrSubsequence(testcase))