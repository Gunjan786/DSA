#Time complexity O(n)
#Space complexity O(1)
#sort array contains only 0's, 1's and 2's
def sort012(arr,n):
    count_0 = 0
    count_1 = 0
    count_2 = 0
        
    i = 0
    j = 0
    while i < n:
        if arr[i] == 0:
            count_0 += 1
        elif arr[i] == 1:
            count_1 += 1
        else:
            count_2 += 1
        i += 1
            
    while j < n:
        if count_0 > 0:
            arr[j] = 0
            count_0 -= 1
        elif count_1 > 0:
            arr[j] = 1
            count_1 -= 1
        else:
            arr[j] = 2
            count_2 -= 1
        j += 1
    return arr
print(sort012([0,1,0,2,1,0], 6))