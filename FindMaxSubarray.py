from collections import namedtuple
Subarray=namedtuple('Subarray', 'low high sum')

def findMaxCrossingSubarray(A,low,mid,high):
    "Find subarray crossing mid, which has maximum sum of elements"
    #[left,mid]
    maxLeft=mid
    leftSum=A[mid]
    sum=A[mid]
    for i in reversed(xrange(low,mid)):
        sum = sum + A[i]
        if sum > leftSum:
            leftSum=sum
            maxLeft = i        
    print A[maxLeft:mid+1], "leftSum:",leftSum, "maxLeft:",maxLeft
    #(mid,right]
    maxRight=mid+1
    rightSum=A[maxRight]
    sum=rightSum
    for i in xrange(mid+2,high+1):
        sum = sum + A[i]
        if sum > rightSum:
            rightSum=sum
            maxRight = i 
    print A[mid+1:maxRight+1]," rightSum: ", rightSum, "maxRight",maxRight
    return Subarray(maxLeft,maxRight,leftSum+rightSum)

def findMaxSubarray(A,low,high):
    "Finds maximum subarray inside array A[low:high]"
    if high == low: #base case: only one element
        return Subarray(low,high,A[low])
    else:
        mid = (low+high)/2
        left = findMaxSubarray(A,low,mid)
        cross = findMaxCrossingSubarray(A,low,mid,high)
        right = findMaxSubarray(A,mid+1,high)
        if left.sum >= cross.sum and left.sum >=right.sum:
            return left
        elif cross.sum >= left.sum and cross.sum >= right.sum:
            return cross
        else:
            return right


A=[1,-5,1000,3,5,-100,7,-8]
maxLeft,maxRight,sum=findMaxCrossingSubarray(A,0,2,5)
print maxLeft,maxRight,sum
print findMaxSubarray(A,0,5)