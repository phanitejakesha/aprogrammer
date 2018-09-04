#LEETCODE Problem number 896
#An array is monotonic if it is either monotone increasing
#or monotone decreasing
#Return true if and only if the given array A is monotonic.

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        mInc = mDec = 0
        for i in range(0,len(A)-1):
            if A[i]<=A[i+1]:
                mInc = mInc+ 1
            if A[i]>=A[i+1]:
                mDec = mDec + 1
        print(mDec,mInc)
        if mDec == len(A)-1 or mInc == len(A)-1:
            return True
        else:
            return False
        
