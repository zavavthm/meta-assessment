# Compute the length of the longest strictly increasing subsequence in a list.
# I/P: [11, 5, 2, 5, 3, 7, 101, 18]
# O/P: 4

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