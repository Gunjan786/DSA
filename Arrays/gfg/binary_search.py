# find k in sorted array
#Time complexity = O(logn)
def binarysearch(arr,n,k):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        
        if k == arr[mid]:
            return mid
        elif k < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(binarysearch([1,2,3,4,5], 5, 5))
