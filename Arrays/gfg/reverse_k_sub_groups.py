#reverse the sub groups of array of size k
#if K > N reverse the array
#Time Complexity O(n) and Space Complexity O(1)
def reverseInGroups(arr, N, K):
    left = 0
    right = K - 1
    right_temp = 0

    while right <= (N-1):
        right_temp = right + 1

        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        left = right_temp
        right = right_temp - 1 + K

    j = right_temp 
    k = N - 1
    while j <= k:
        arr[j], arr[k] = arr[k], arr[j]
        j += 1
        k -= 1

    return arr

print(reverseInGroups([1,2,3,4,5], 5, 3))        