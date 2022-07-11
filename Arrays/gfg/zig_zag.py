#Time Complexity O(n)
#Space Complexity O(1)
#convert the array into  a < b > c < d > e < f form
def zigZag(arr, n):
    min = 0
    max = 1
    i = 0
    while i < n-1:
        if min % 2 == 0 and arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        elif max % 2 == 0 and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        min += 1
        max += 1
        i += 1
    return arr
print(zigZag([1,2,3,4,5],5))