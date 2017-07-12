def findMaxCrossingSubarray(A,left,mid,right):
    "Find subarray crossing mid, which has maximum sum of elements"
    #[left,mid]
    maxLeft=mid
    leftSum=A[mid]
    sum=A[mid]
    for i in reversed(xrange(left,mid)):
        sum = sum + A[i]
        if sum > leftSum:
            leftSum=sum
            maxLeft = i        
    print A[maxLeft:mid+1], "leftSum:",leftSum, "maxLeft:",maxLeft
    #(mid,right]
    maxRight=mid
    rightSum=A[mid+1]
    sum=A[mid+1]
    for i in xrange(mid+2,right+1):
        sum = sum + A[i]
        if sum > rightSum:
            rightSum=sum
            maxRight = i 
    print A[mid+1:maxRight+1]," rightSum: ", rightSum, "maxRight",maxRight
    return maxLeft,maxRight,leftSum+rightSum
    
A=[1,-5,3,5,7,-8]

print(findMaxCrossingSubarray(A,0,2,5))