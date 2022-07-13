class Solution(object):
    def maxSubArray(self, nums):
        currsum = 0
        maxsum = -99999999
        
        for num in nums:
            currsum+=num
            if maxsum<currsum:
                maxsum=currsum
            if currsum<0:
                currsum=0
            return maxsum
        

class Solution:
   
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
